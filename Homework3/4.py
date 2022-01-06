def my_func(x, y):
    i = 1
    while i < y:
        x *= x
        i += i
        return x


print(my_func(5, 2))
