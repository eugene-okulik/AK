person = ['John', 'Doe', 'New York', '+1372829383739', 'US']


name, last_name, city, phone, country = person


print(name, last_name, city, phone, country)


massage_1 = 'результат операции: 42'


massage_2 = 'результат операции: 514'


massage_3 = 'результат работы программы: 9'


massage_index_1 = massage_1[19:]


massage_index_2 = int(massage_2.index(':')) + 1


massage_index_3 = int(massage_3.index(':')) + 1


print(int(massage_index_1) + 10)  # свой вариант без index


print(int(massage_2[massage_index_2:]) + 10)


print(int(massage_3[massage_index_3:]) + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']


subjects = ['math', 'biology', 'geography']


print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
