def my_func(a, b, c):
    my_func_list = [a, b, c]
    for el in my_func_list:
        if a > c and b > c:
            return a + b
        elif b > a and c > a:
            return b + c
        elif a > b and c > b:
            return a + c


print(my_func(15, 26, 80))
