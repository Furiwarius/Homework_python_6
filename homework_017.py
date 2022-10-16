# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from random import randrange

# было
def simple_multiplier_1(value):
    mult_list = []
    for i in range(2,value):
        while value%i==0:
            value/=i
            mult_list.append(i)
    return mult_list

N = randrange(50, 5000)
print(N)
print(simple_multiplier_1(N))

#стало
# Во втором номере можно тратить меньше ресурсов, если проверять i*i <=n, дополнительно можно почитать тут про другие способы нахождения простых делителей: https://habr.com/ru/post/468833/

def simple_multiplier_2(value):
    mult_list = []
    while value%2==0:
        value//=2
        mult_list.append(2)
    for i in range(3,value+1,2):
        while value%i==0:
            value//=i
            mult_list.append(i)
    return mult_list

print(simple_multiplier_2(N))