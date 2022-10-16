# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

from random import randrange

# было
def creating_originality(new_list):
    rezult_list = []
    for val in new_list:
        if val not in rezult_list: rezult_list.append(val)
    return rezult_list


random_list = [randrange(1,10) for _ in range(20)]
print(random_list)
print(creating_originality(random_list))

# или 
print(set(random_list))



# стало
# В третьем можно подумать, как сделать вариант, где уникальным является тот элемент, который встречается только один раз в первоначальном cпиcке

result_list = [val for val in random_list if random_list.count(val)==1]
print(result_list)



