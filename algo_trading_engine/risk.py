from config import RISK_PER_TRADE, MAX_POSITION_SIZE, MAX_DAILY_LOSS

class RiskManager:
    def __init__(self, initial_capital):
        self.initial_capital = initial_capital
        self.daily_pnl = 0.0

    def position_size(self, cash, price):
        size = int((cash * RISK_PER_TRADE) / price)
        return min(size, MAX_POSITION_SIZE)

    def check_order(self, quantity):
        return abs(quantity) <= MAX_POSITION_SIZE

    def update_pnl(self, pnl):
        self.daily_pnl += pnl
        if self.daily_pnl <= -self.initial_capital * MAX_DAILY_LOSS:
            raise RuntimeError("DAILY LOSS LIMIT BREACHED")
