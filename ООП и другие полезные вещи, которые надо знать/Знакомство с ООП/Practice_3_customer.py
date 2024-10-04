class Customer:
    def __init__(self, name):
        self.name = name
        self.__discount = 10

    def get_price(self, price: float) -> float:
        return round(price * (1 - self.__discount / 100), 2)

    def set_discount(self, new_discount: int) -> None:
        self.__discount = new_discount if new_discount < 80 else 80


customer = Customer("Иван Иванович")
print(customer.get_price(100))
customer.set_discount(20)
print(customer.get_price(100))
