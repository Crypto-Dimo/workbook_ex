print('\nCelsius | Fahrenheit')
print('--------------------')

for degree in range(0, 100, 10):
    fahrenheit = int((degree * 9 / 5) + 32)
    print(f'{degree:^7} | {fahrenheit:^11}')
    print('--------------------')
