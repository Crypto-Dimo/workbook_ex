less_than_2 = 0.00
three_to_12 = 14.00
twelve_to_65 = 23.00
over_65 = 18.00

guest = input('Enter your age: ')
price_list = []

while guest != '':
    guest = float(guest)
    if guest <= 2:
        price = less_than_2
    elif 3 <= guest <= 12:
        price = three_to_12
    elif guest >= 65:
        price = over_65
    elif 12 < guest < 65:
        price = twelve_to_65
    price_list.append(price)
    guest = input('Enter your age (enter blank to end): ')

if guest == '':
    total_price = sum(price_list)
    print(f'The total amount due for this group is: $ {round(total_price, 2)}')