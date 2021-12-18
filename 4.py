num = input('Enter number : ')
var1 = int(num)
res1 = var1 // 100
var2 = var1 % 100
res2 = var2 // 10
res3 = var1 % 10
mx = res1

while True:
    if res2 > mx:
        mx = res2
    if res3 > mx:
        mx = res3
    print(mx)
    break
