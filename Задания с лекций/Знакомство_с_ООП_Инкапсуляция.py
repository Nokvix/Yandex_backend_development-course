class Employee:
    vacation_days: int = 28

    def __init__(self, first_name: str, second_name: str, gender: str) -> None:
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.gender: str = gender
        self.remaining_vacation_days: int = Employee.vacation_days
        self._employee_id: int = self.__generate_employee_id()

    def __generate_employee_id(self) -> int:
        return hash(self.first_name + self.second_name + self.gender)

    def consume_vacation(self, days) -> None:
        self.remaining_vacation_days -= days

    def get_vacation_details(self) -> str:
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):
    def __init__(self, first_name: str, second_name: str,
                 gender: str, salary: int) -> None:
        super().__init__(first_name, second_name, gender)
        self.__salary = salary

    def __get_vacation_salary(self) -> float:
        return self.__salary * 0.8

    def get_unpaid_vacation(self, start_date: str, number_days: int) -> str:
        return (
            f'Начало неоплачиваемого отпуска: {start_date}, '
            f'продолжительность: {number_days} дней.')


class PartTimeEmployee(Employee):
    vacation_days: int = 14

    def __init__(self, first_name: str, second_name: str, gender: str):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days: int = self.vacation_days


full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
full_time_employee.consume_vacation(4)
print(full_time_employee.get_unpaid_vacation('2021-03-10', 12))
print(full_time_employee.get_vacation_details())
print(full_time_employee._employee_id)
print(full_time_employee.__salary)
print(full_time_employee.__generate_employee_id())
print(full_time_employee.__get_vacation_salary())


part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
part_time_employee.consume_vacation(5)
print(part_time_employee.get_vacation_details())
print(part_time_employee._employee_id)
print(part_time_employee.__generate_employee_id())
