decimal = int(input('Enter the decimal number: '))

q = decimal
result = ''

while q != 0:
    r = q % 2
    result = str(r) + result
    q = q // 2

print(f'The binary corresponding to {decimal} is: {result}.')
