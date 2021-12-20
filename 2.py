sec = input('Set time in seconds = ')

x = int(sec)
y = x % 3600
hours = x // 3600
minutes = y // 60
seconds = y % 60

print(f'The estimate time is {hours:02d}:{minutes:02d}:{seconds:02d}')
