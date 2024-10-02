class Employee:
    vacation_days: int = 28

    def __init__(self, first_name: str, second_name: str, gender: str) -> None:
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.gender: str = gender

    def __str__(self) -> str:
        return (
            f'Имя: {self.first_name}, '
            f'Фамилия: {self.second_name}, '
            f'Пол: {self.gender}, '
            f'Отпускных дней в году: {self.vacation_days}.'
        )


employee1: Employee = Employee(
    first_name='Роберт',
    second_name='Крузо',
    gender='м'
)

employee2: Employee = Employee(
    first_name='Мария',
    second_name='Крузова',
    gender='ж'
)

print(employee1)
print(employee2)
