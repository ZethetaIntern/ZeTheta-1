import numpy as np


class Rebalancer:
    @staticmethod
    def rebalance(current, target, tax_rate=0.2, txn_cost=0.001):
        trades = target - current

        transaction_cost = np.sum(np.abs(trades)) * txn_cost
        tax_cost = np.sum(np.maximum(trades, 0)) * tax_rate

        net_trades = trades * (1 - transaction_cost - tax_cost)
        return net_trades
