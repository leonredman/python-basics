# range() function 

'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

years = int(input('Enter years:\n'))

savings = initial_savings
for i in range(years):
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate)

print('\n')


''' yield:
Enter years: 8
 Savings in year 0: $10000.000000
 Savings in year 1: $10500.000000
 Savings in year 2: $11025.000000
 Savings in year 3: $11576.250000
 Savings in year 4: $12155.062500
 Savings in year 5: $12762.815625
 Savings in year 6: $13400.956406
 Savings in year 7: $14071.004227
'''