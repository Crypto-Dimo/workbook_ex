m = float(input('Enter the first value: '))
n = float(input('Enter the second value: '))
d = min(m, n)

while m % d != 0 or n % d != 0:
    d -= 1
print(f'The greatest common divisor of {m} and {n} is: {d}')

