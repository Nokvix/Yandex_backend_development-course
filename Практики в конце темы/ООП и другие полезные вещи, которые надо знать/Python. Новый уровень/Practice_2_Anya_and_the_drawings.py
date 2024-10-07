from datetime import datetime
from random import sample


def choose_days() -> None:
    first_month_half = list(range(1, 16))

    random_days = sample(first_month_half, k=3)
    sorted_days = sorted(random_days)

    now = datetime.now()

    for i in range(3):
        practice_day = now.replace(day=sorted_days[i]).strftime("%d.%m.%Y")
        print(f'{i + 1}-е занятие: {practice_day}')


choose_days()
