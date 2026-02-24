import pandas as pd

def classify_regime(market_returns: pd.Series, window: int = 63) -> pd.Series:
    rolling_mean = market_returns.rolling(window).mean()
    regime = rolling_mean.apply(lambda x: 1 if x > 0 else -1)
    return regime

def regime_performance(strategy_returns: pd.Series,
                       regime_series: pd.Series) -> pd.DataFrame:
    
    df = pd.concat([strategy_returns, regime_series], axis=1)
    df.columns = ["returns", "regime"]
    
    bull = df[df["regime"] == 1]["returns"]
    bear = df[df["regime"] == -1]["returns"]
    
    return pd.DataFrame({
        "Bull_Return": [bull.mean() * 252],
        "Bear_Return": [bear.mean() * 252]
    })