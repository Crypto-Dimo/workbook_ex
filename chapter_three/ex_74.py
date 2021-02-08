x = float(input('Enter the number: '))

guess = x / 2

precision = 10 ** (-12)

while abs(x - guess * guess) > precision:
    guess = (guess + x / guess) / 2

print(guess)





