n = int(input('Enter a number that is >= 2: '))

factor = 2
active = True

if n < 2:
    active = False
    print('Invalid value.')
else:
    print(f'The prime factors of {n} are:')

while factor <= n and active:
    if n % factor == 0:
        print(factor)
        n = n // factor
    else:
        factor += 1
