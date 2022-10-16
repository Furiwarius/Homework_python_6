# Вычислить число c заданной точностью d

from decimal import Decimal

from random import uniform

# было
def obtaining_accuracy_1():
    while True:
        try:
            value = input("Задайте необходимую точность для случайного числа: ")
            float(value)
        except ValueError:
            print("Введенное число не подходит, попробуйте заново")
            continue
        break
    return str(value)

random_number = float(uniform(1,100))
print(random_number)

value = obtaining_accuracy_1()
rezult_value = Decimal(random_number).quantize(Decimal(value))
print(rezult_value)

# стало
# В первом номере рекомендую подумать, как можно обрубать число(т.е. доводить до какого-то знака, а не округлять) (замечания преподавателя)

def obtaining_accuracy_2():
    while True:
        try:
            value = input("Задайте необходимую точность для случайного числа: ")
            float(value)
        except ValueError:
            print("Введенное число не подходит, попробуйте заново")
            continue
        break
    return len(value[value.find('.'):])


print('-----------------------------------')
print(random_number)
exact_number = str(random_number)[:str(random_number).find('.')+obtaining_accuracy_2()]
print(exact_number)


