import random

max_num = random.randint(1, 100)
print(max_num)
counts = 0

for i in range(1, 99):
    next_num = random.randint(1, 100)
    if next_num > max_num:
        counts += 1
        max_num = next_num
        print(f'{max_num} - Total counts {counts}')
    else:
        print(next_num)

print(f'Te maximum value encountered was {max_num}.')
print(f'The maximum value was updated {counts} times.')

# Using lists & shuffle to avoid repetition and missing numbers in range 1-100

num_list = []

for i in range(1, 101):
    num_list.append(i)
    random.shuffle(num_list)

max_num = num_list[0]
counts = 0

for n in num_list:
    if n > max_num:
        counts += 1
        print(f'{n} - Total counts {counts}')
        max_num = n
    else:
        print(n)

print(f'Te maximum value encountered was {max_num}.')
print(f'The maximum value was updated {counts} times.')

