my_list = [7, 5, 3, 3, 2]
num = int(input('Your number: '))
i = 0

for elem in my_list:
    if num <= elem:
        i += 1
    elif num > elem:
        break
my_list.insert(i, num)
print(my_list)
