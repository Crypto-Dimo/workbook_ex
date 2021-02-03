original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount = 60

for price in original_prices:
    discount_amount = (price * discount / 100)
    discounted_price = price - discount_amount
    print(f'\nOriginal price: {price:>6}$')
    print(f'Discount: {-round(discount_amount, 2):>12}$')
    print(f'Discounted price: {round(discounted_price, 2)}$')
