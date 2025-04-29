import random


while True:
    salary = int(input('Зарплата: '))
    bonus_value = [True, False]
    bonus = bool(random.choice(bonus_value))
    random_bonus = random.randint(0, 1000)

    if bonus is True:
        finish_salary = salary + random_bonus
    else:
        finish_salary = salary
    print(f"{salary}, {bonus} - '${finish_salary}'")
