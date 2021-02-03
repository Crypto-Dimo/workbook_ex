# my solution

import math

shopping_active = True

items = []

while shopping_active:
    item = float(input('Enter the item price (enter 0 to end): '))
    items.append(item)
    total_cost = sum(items)
    if item == 0:
        shopping_active = False
        total_in_pennies = total_cost * 100
        round_to_nickel = total_in_pennies % 5
        if round_to_nickel < 2.5:
            rounded_down = math.floor(total_cost / 0.05) * 0.05
            print(f'The total amount for the shopping is: {round(total_cost, 2)}$')
            print(f'The total rounded amount for the shopping is: {round(rounded_down, 2)}$')
        else:
            rounded_up = math.ceil(total_cost / 0.05) * 0.05
            print(f'The total amount for the shopping is: {round(total_cost, 2)}$')
            print(f'The total rounded amount is: {round(rounded_up, 2)}$')


# workbook solution

pennies_per_nickel = 5
nickel = 0.05

total = 0.00

line = input('Enter the item price (blank to end): ')

while line != '':
    total = total + float(line)
    line = input('Enter the item price (blank to end): ')

print(f'The total amount for the shopping is: {round(total, 2)}$')

rounding_indicator = total * 100 % pennies_per_nickel

if rounding_indicator < pennies_per_nickel / 2:
    cash_total = total - rounding_indicator / 100
else:
    cash_total = total + nickel - rounding_indicator / 100

print(f'The total rounded amount is: {round(cash_total, 2)}$')
