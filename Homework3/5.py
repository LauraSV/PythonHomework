def ms_text():
    num_list = input('Введите числа через пробел: ').split()
    sum_el = 0
    for num in num_list:
        sum_el += int(num)
    print(sum_el)


print(ms_text())

