import time
import pandas as pd
from config import *
from strategy import MovingAverageStrategy
from risk import RiskManager
from oms import OrderManager
from portfolio import Portfolio
from execution import create_exchange
from data import prepare_dataframe

exchange = create_exchange(EXCHANGE)

strategy = MovingAverageStrategy()
risk = RiskManager(INITIAL_CAPITAL)
oms = OrderManager()
portfolio = Portfolio(INITIAL_CAPITAL)

print(" Live paper trading started")

while True:
    ohlcv = exchange.fetch_ohlcv(SYMBOL, timeframe=TIMEFRAME, limit=50)
    df = prepare_dataframe(ohlcv)
    price = df["close"].iloc[-1]

    signal = strategy.generate_signal(df, portfolio.position)

    if signal in ["BUY", "SELL"]:
        size = risk.position_size(portfolio.cash, price)
        qty = size if signal == "BUY" else -portfolio.position

        if qty != 0:
            order = oms.create_order(signal, qty, price)
            order["status"] = "FILLED"
            portfolio.update(qty, price)
            print(f"{signal} {abs(qty)} @ {price}")

    equity = portfolio.equity(price)
    print(f"Equity: {round(equity,2)}")

    time.sleep(30)
