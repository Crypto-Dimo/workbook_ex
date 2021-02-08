MIN = 1
MAX = 11

print('\t\t| 1\t\t| 2\t\t| 3\t\t| 4\t\t| 5\t\t| '
      '6\t\t| 7\t\t| 8\t\t| 9\t\t| 10\t|')
print('---------------------------------------------'
      '--------------------------------------------')
for a in range(MIN, MAX):
    print(f'{a}', '\t\t|', a * 1, '\t|', a * 2, '\t|', a * 3,
          '\t|', a * 4, '\t|', a * 5, '\t|', a * 6, '\t|', a * 7,
          '\t|', a * 8, '\t|', a * 9, '\t|', a * 10, '\t|')
    print('---------------------------------------------'
          '--------------------------------------------')

# workbook (I used 'f-strings' instead and '\t' for spacing)

MIN = 1
MAX = 10

print('    ', end='')

# top row table
for i in range(MIN, MAX + 1):
    print(f'\t\t{i}', end='')
print()
# table
for i in range(MIN, MAX + 1):
    print(f'\t{i}', end='')
    for j in range(MIN, MAX + 1):
        print(f'\t\t{i * j}', end='')
    print()
