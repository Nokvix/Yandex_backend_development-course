def fibonacci(n):
    previous_number = 0
    current_number = 1

    for _ in range(n):
        yield previous_number

        next_number = previous_number + current_number
        previous_number, current_number = current_number, next_number


sequence = fibonacci(6)
for number in sequence:
    print(number)
