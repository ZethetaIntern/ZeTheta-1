class Portfolio:
    def __init__(self, capital):
        self.cash = capital
        self.position = 0
        self.equity_curve = []

    def update(self, quantity, price):
        self.position += quantity
        self.cash -= quantity * price

    def equity(self, price):
        eq = self.cash + self.position * price
        self.equity_curve.append(eq)
        return eq
