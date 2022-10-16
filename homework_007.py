# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Было
import random
import math

def multiplication(value):
    new_list = []
    for i in range(1, value+1):
        new_list.append(math.factorial(i))
    return new_list


value = random.randrange(1, 10)
print(value)
print(multiplication(value))

# Стало

print(value)
print([math.factorial(val) for val in range(1, value+1)])
