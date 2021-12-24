while True:
    num = int(input('Enter the number of the month: '))
    if 0 < num <= 12:
        list1 = ['winter', 'spring', 'summer', 'autumn', 'winter']
        print(list1[num // 3])
        break
    else:
        print('Enter number please')

while True:
    num = int(input('Enter the number of the month: '))
    if 0 < num <= 12:
        dict1 = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn', 4: 'winter'}
        print(dict1[num // 3])
        break
    else:
        print('Enter number please')
