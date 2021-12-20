revenue = input('How much your revenue is = ')
costs = input('Your total costs is = ')

revenue_1 = int(revenue)
costs_1 = int(costs)

if revenue_1 > costs_1:
    print('Congrats!')
    profit = revenue_1 - costs_1
    rent = profit / revenue_1
    num = int(input('Your number of employees is = '))
    prof_employees = profit / num
    print(f'You have finished your year with {profit}$ in profit. The profitability of your '
          f'busines is {rent}. The total profit for one employee is {prof_employees:.02f}')
else:
    print("It's sad")
