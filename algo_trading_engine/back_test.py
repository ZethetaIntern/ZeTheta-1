from data import prepare_dataframe

def run_backtest(df, strategy, risk, portfolio, oms):
    for i in range(len(df)):
        price = df["close"].iloc[i]
        signal = strategy.generate_signal(df.iloc[: i + 1], portfolio.position)

        if signal in ["BUY", "SELL"]:
            size = risk.position_size(portfolio.cash, price)
            qty = size if signal == "BUY" else -portfolio.position

            if qty != 0 and risk.check_order(qty):
                order = oms.create_order(signal, qty, price)
                order["status"] = "FILLED"
                portfolio.update(qty, price)

        portfolio.equity(price)

    return portfolio.equity_curve
