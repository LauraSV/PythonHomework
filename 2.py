data = input('Input data list using space characters: ').split(' ')
for elem in range(1, len(data), 2):
    data[elem-1], data[elem] = data[elem], data[elem-1]
print(data)
