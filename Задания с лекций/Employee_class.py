class Employee:
    vacation_days: int = 28

    def __init__(self, first_name: str, second_name: str, gender: str) -> None:
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.gender: str = gender
        self.remaining_vacation_days: int = self.vacation_days

    def __str__(self) -> str:
        return (
            f'Имя: {self.first_name}, '
            f'Фамилия: {self.second_name}, '
            f'Пол: {self.gender}, '
            f'Отпускных дней в году: {self.vacation_days}.'
        )

    def consume_vacation(self, write_off_days: int) -> None:
        self.remaining_vacation_days -= write_off_days

        if self.remaining_vacation_days < 0:
            self.remaining_vacation_days = 0

    def get_vacation_details(self) -> str:
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(7)
print(employee.get_vacation_details())
