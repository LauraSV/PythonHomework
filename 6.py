a = 2
b = 3
count = 0

while a < b:
    count += 1
    print(f'day {count} : {a:.2f}')
    a = 1.1 * a
else:
    print(f'day {count+1} : {a:.2f}')

print(f'On day {count+1} the athlete achieved a result of more then 3 km ')
