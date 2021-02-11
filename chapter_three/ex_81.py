binary = input('Enter the binary number: ')

x = len(binary)
result = 0
for digit in binary:
    x -= 1
    decimal = int(digit) * 2 ** x
    result = result + decimal
print(f'The equivalent decimal number of {binary} is: {result}.')

