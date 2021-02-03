numbers = []

computing_active = True

while computing_active:
    number = float(input('Enter the number (enter 0 to quit): '))
    if number != 0:
        numbers.append(number)
        if len(numbers) < 2:
            continue
        else:
            average = sum(numbers) / 2
            print(f'The average of {numbers} is:\n- {average}')
    else:
        print('Till next time, bye!')
        computing_active = False
