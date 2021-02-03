inches_or_meters = input('Are you using inches or meters? ')

if inches_or_meters == 'inches':
    height = float(input('Height: '))
    weight = float(input('Weight: '))
    BMI = weight / (height ** 2) * 703
    print('Your BMI is: ', round(BMI, 2))
else:
    height = float(input('Height: '))
    weight = float(input('Weight: '))
    BMI = weight / (height ** 2)
    print('Your BMI is: ', round(BMI, 2))