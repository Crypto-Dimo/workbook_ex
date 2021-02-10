n = int(input('Enter a value: '))

print('Sequence: ', end=' ')
print(n, end=' ')

while n > 1:
    if n % 2 == 0:
        n = n // 2
        print(n, end=' ')
    else:
        n = 3 * n + 1
        print(n, end=' ')
    if n == 1:
        n = int(input('\nEnter a value (0 to end): '))
        if n != 0:
            print('Sequence: ', end=' ')
            print(n, end=' ')
        elif n == 0:
            print('\nEnd of Program.')

