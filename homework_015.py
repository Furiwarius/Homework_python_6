# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. F n = F n − 1 + F n − 2

from random import randrange

# было
new_list = [0, 1]

def definition_negative(value, number):
    if number%2:return -value
    return value

for number in range(2,randrange(5, 20)):
    new_list.append(new_list[number-1]+new_list[number-2])
else:
    new_list = [definition_negative(val, n) for n, val in enumerate(new_list[:0:-1])] + new_list
print(new_list)

# стало
# # 2) Как доп, подумать как сделать рекурсией (замечания преподавателя)

new_list = [0, 1]

def definition_negative(value, number):
    if number%2:return -value
    return value

def fibonacci_with_recursion(new_list, n_number, index=len(new_list)):
    if index == n_number:
        return new_list
    new_list.append(new_list[index-1]+new_list[index-2])
    fibonacci_with_recursion(new_list, n_number, len(new_list))


fibonacci_with_recursion(new_list, randrange(10, 20))
new_list = [definition_negative(val, n) for n, val in enumerate(new_list[:0:-1])] + new_list
print(new_list)

