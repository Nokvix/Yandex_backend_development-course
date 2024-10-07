class Product:
    def __init__(self, product_name: str, quantity: int) -> None:
        self.product_name = product_name
        self.quantity = quantity

    def get_info(self) -> str:
        return f'{self.product_name} (в наличии: {self.quantity})'


class Kettlebell(Product):
    def __init__(self, product_name: str, quantity: int,
                 weight: float) -> None:
        super().__init__(product_name, quantity)
        self.weight = weight

    def get_weight(self) -> str:
        new_string: str = f'{self.get_info()}. Вес: {self.weight} кг'
        return new_string


class Clothing(Product):
    def __init__(self, product_name: str, quantity: int, size: str) -> None:
        super().__init__(product_name, quantity)
        self.size = size

    def get_size(self) -> str:
        new_string: str = f'{self.get_info()}. Размер: {self.size}'
        return new_string


small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
