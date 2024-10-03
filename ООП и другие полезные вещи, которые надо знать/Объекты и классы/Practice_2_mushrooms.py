from typing import List


class MushroomsCollector:
    def __init__(self) -> None:
        self.mushrooms: List[str] = []

    def is_poisonous(self, mushroom_name: str) -> bool:
        if mushroom_name == 'Мухомор' or mushroom_name == 'Поганка':
            return True
        return False

    def add_mushroom(self, mushroom_name: str):
        if self.is_poisonous(mushroom_name=mushroom_name):
            print('Нельзя добавить ядовитый гриб')
        else:
            self.mushrooms.append(mushroom_name)

    def __str__(self) -> str:
        result: str = ', '.join(self.mushrooms)
        return result


collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
print(collector_1)
print(collector_2)
