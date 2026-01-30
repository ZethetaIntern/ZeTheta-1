class MovingAverageStrategy:
    def __init__(self, short_window=5, long_window=15):
        self.short = short_window
        self.long = long_window

    def generate_signal(self, df, position):
        if len(df) < self.long:
            return "HOLD"

        short_ma = df["close"].rolling(self.short).mean().iloc[-1]
        long_ma = df["close"].rolling(self.long).mean().iloc[-1]

        if short_ma > long_ma and position == 0:
            return "BUY"
        if short_ma < long_ma and position > 0:
            return "SELL"
        return "HOLD"
