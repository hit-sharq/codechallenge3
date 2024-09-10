class Coffee:
    def __init__(self, name):
        self.name = name
        self._order_count = 0  # to track the number of orders for this coffee
        self._total_price = 0.0  # to track the total price of all orders for this coffee

    def num_orders(self):
        return self._order_count

    def increment_orders(self, price):
        self._order_count += 1  # increments the order count each time an order is made
        self._total_price += price  # add the price of this order to the total price

    def average_price(self):
        if self._order_count == 0:
            return 0.0  # Avoid division by zero
        return self._total_price / self._order_count  # Calculate the average price

class Customer:
    def __init__(self, name):
        self.name = name

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        coffee.increment_orders(price)  # Increment order count and add the price for the coffee
        return order

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price