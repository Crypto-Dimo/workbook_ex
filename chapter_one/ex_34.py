# loaf of bread = $3.49
# day old loaf = -60%

old_loaves_bread = int(input('How many loaves? '))

regular_price = 3.49 * old_loaves_bread
discount = regular_price * 60 / 100
total = regular_price - discount

print('Regular price:', f'{round(regular_price, 2):>8}', '$')
print('Discount:', f'{round(discount, 2):>13}', '$')
print('Total price:', f'{round(total, 2):>10}', '$')