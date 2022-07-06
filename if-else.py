# if - else

price_younger = 4800  # Age less than 25
price_older = 2200  # Age 25 and up

age = int(input('Enter age:\n'))

if age < 25:
    price = price_younger
    print('EXECUTED FIRST BRANCH')
else:
    price = price_older
    print('EXECUTED SECOND BRANCH')

print('Annual price: $%d' % price)