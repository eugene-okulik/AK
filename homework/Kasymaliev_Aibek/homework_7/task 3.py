massage_1 = 'результат операции: 42'
massage_2 = 'результат операции: 514'
massage_3 = 'результат работы программы: 9'


def massage_result(massage_for_function):
    massage_index = int(massage_for_function.index(':')) + 1
    print(massage_index + 10)


massage_result(massage_1)
massage_result(massage_2)
massage_result(massage_3)
