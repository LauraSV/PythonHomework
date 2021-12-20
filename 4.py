'''num = input('Enter number : ')
num = int(num)
res1 = num // 10
var2 = num % 10
res2 = var2 // 10
res3 = num % 10
mx = res1

while True:
    if res2 > mx:
        mx = res2
    if res3 > mx:
        mx = res3
    print(mx)
    break'''

num = int(input('Enter number : '))
maxInt = 0

while num != 0:
    newNum = num % 10
    if newNum > maxInt:
        maxInt = newNum
    num = num // 10
print(maxInt)

