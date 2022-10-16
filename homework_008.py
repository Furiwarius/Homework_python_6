# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

import random

# Было

def generator(random_number):
    new_list = []
    for i in range(1, random_number+1):
        value = round((1+1/i)**i)
        new_list.append(value)
    return new_list

random_number = random.randrange(5,20)
new_list = generator(random_number)
print(new_list)
print(sum(new_list))

# Стало

new_list = [round((1+1/i)**i) for i in range(1, random_number+1)]
print(new_list)
print(sum(new_list))
