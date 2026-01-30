class OrderManager:
    def __init__(self):
        self.orders = []

    def create_order(self, side, quantity, price):
        order = {
            "side": side,
            "quantity": quantity,
            "price": price,
            "status": "NEW"
        }
        self.orders.append(order)
        return order
