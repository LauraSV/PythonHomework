num = int(input('Enter number : '))
maxInt = 0

while num != 0:
    newNum = num % 10
    if newNum > maxInt:
        maxInt = newNum
    num = num // 10
print(maxInt)

