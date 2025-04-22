import random

random_number = random.randint(1, 10)
print(random_number)


user_number = int(input('Введите число: '))


while user_number != random_number:
    print('попробуйте снова')
    user_number = int(input('Введите число: '))


print('Поздравляю! Вы угадали!')
