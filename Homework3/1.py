first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))


def func(first_number, second_number):
    if second_number != 0:
        print(first_number / second_number)
    else:
        print('На ноль делить НЕЛЬЗЯ')


func(first_number, second_number)