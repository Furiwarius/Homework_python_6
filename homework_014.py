# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# было

new_list = [value for value in range(10)]
print(f"набор цифр: {new_list}")
bin_list = [bin(val)[2:] for val in new_list]
print(f"перевод в двоичную систему с помощью bin(): {bin_list}")


#стало
# 1) 4-ый номер принят (рекомендую посмотреть как решить без использования встроенной функции, если знаете, то отлично) (замечания преподавателя)
# 2) Как доп, подумать как сделать рекурсией (замечания преподавателя)


def bin_translation_1(value):
    # без использования встроенных функций

    if value==0:
        return '0'
    rezult_str=''
    while value>0:
        rezult_str = str(value%2)+rezult_str
        value//=2
    return rezult_str


def bin_translation_2(value):
    # с использованием рекурсии

    global rezult
    if value==0 and len(rezult)==0:
        rezult.append(str(0))
    if value>0:
        rezult.append(str(value%2))
        bin_translation_2(value//2)
    return rezult
        

print(f"перевод в двоичную систему без встроенных функций и рекурсии: {list(map(bin_translation_1, new_list))}")

f_list = []
for val in new_list:
    rezult=[]
    f_list.append(''.join(bin_translation_2(val)[::-1]))
else:
    print(f"перевод в двоичную систему с помощью рекурсии: {f_list}")
