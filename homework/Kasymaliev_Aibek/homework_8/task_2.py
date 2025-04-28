import sys


sys.set_int_max_str_digits(1000001)


def fib_funct(limit=100001):
    first_num = 0
    second_num = 1
    count = 0
    while count < limit:
        yield count, first_num
        first_num, second_num = second_num, first_num + second_num
        count += 1


for count, value in fib_funct(100001):
    if count in (5, 200, 1000, 100000):
        print(f"Fibonacci number at position {count} is {value}")
