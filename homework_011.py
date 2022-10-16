# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# было

from random import  randrange

def odd_sum(new_list):
    result = 0
    for i, value in enumerate(new_list):
        if (i+1)%2!=0: result+=value
    return result

new_list = [value for value in range(1,randrange(10,20))]
print(new_list)
print(odd_sum(new_list))

# стало

print(new_list)
sum_list = sum(new_list[::2])
print(sum_list)