def decorator_func(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = '*'
            func(first, second, operation)
        elif first == second:
            operation = '+'
            func(first, second, operation)
        elif first > second:
            operation = '-'
            func(first, second, operation)
        elif second > first:
            operation = '/'
            func(first, second, operation)

        return func(first, second, operation)

    return wrapper


@decorator_func
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second > 0:
            return first / second


first = int(input('Введите первое число:'))
second = int(input('Введите второе число:'))
operation = 0

result = calc(first, second, operation)
print(f'Полученный результат: {result}')
