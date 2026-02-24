import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import plotly.express as px
import pandas as pd

from src.data_loader import load_strategy_returns, load_market_data
from src.performance import sharpe_ratio
from src.statistics import sharpe_significance_test
from src.risk import compute_drawdown, max_drawdown
from src.regimes import classify_regime, regime_performance
from src.correlation import correlation_matrix
from src.capacity import estimate_capacity
from src.ranking import strategy_ranking

st.set_page_config(layout="wide")
st.title("Quantitative Risk Dashboard")

strategy_df = load_strategy_returns("data/strategy_returns_large.csv")
market_df = load_market_data("data/market_data_large.csv")

strategy = st.selectbox("Select Strategy", strategy_df.columns)

returns = strategy_df[strategy]

# Performance Metrics
sharpe = sharpe_ratio(returns)
z, p = sharpe_significance_test(sharpe, len(returns))
mdd = max_drawdown(returns)

col1, col2, col3 = st.columns(3)
col1.metric("Sharpe Ratio", round(sharpe, 3))
col2.metric("Sharpe p-value", round(p, 5))
col3.metric("Max Drawdown", round(mdd, 3))

# Drawdown Chart
dd = compute_drawdown(returns)
fig_dd = px.line(dd, title="Drawdown Curve")
st.plotly_chart(fig_dd, use_container_width=True)

# Correlation Heatmap
st.subheader("Strategy Correlation Matrix")
corr = correlation_matrix(strategy_df)
fig_corr = px.imshow(corr, text_auto=True)
st.plotly_chart(fig_corr, use_container_width=True)

# Regime Performance
st.subheader("Regime Performance")
regime_series = classify_regime(market_df["market_return"])
reg_perf = regime_performance(returns, regime_series)
st.dataframe(reg_perf)

# Capacity Estimation
st.subheader("Capacity Estimation")
turnover = st.slider("Turnover Assumption", 0.1, 2.0, 0.5)
avg_vol = market_df["avg_daily_volume"].mean()
capacity = estimate_capacity(avg_vol, turnover)
st.metric("Estimated Capacity ($)", round(capacity, 2))

# Strategy Ranking
st.subheader("Strategy Ranking")
rank_table = strategy_ranking(strategy_df)
st.dataframe(rank_table)