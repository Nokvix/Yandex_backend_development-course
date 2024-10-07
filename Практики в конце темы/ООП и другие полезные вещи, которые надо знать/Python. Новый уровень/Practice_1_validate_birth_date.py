from datetime import datetime
from typing import Dict, List, Tuple


def validate_record(name: str, birth_date: str) -> bool:
    try:
        datetime.strptime(birth_date, '%d.%m.%Y')
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {birth_date}')
        return False
    else:
        return True


def process_people(data: List[Tuple[str, str]]) -> Dict[str, int]:
    good_count = 0
    bad_count = 0

    for name, birth_date in data:
        if validate_record(name, birth_date):
            good_count += 1
        else:
            bad_count += 1

    return {'good': good_count, 'bad': bad_count}


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics: Dict[str, int] = process_people(data)

print(f'Корректных записей: {statistics["good"]}\n'
      f'Некорректных записей: {statistics["bad"]}')
