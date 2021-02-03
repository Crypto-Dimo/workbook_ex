feet = float(input('How many feet? '))
inches = float(input('How many inches? '))

feet_to_cm = feet * 30.48
inches_to_cm = inches * 2.54

height_in_cm = feet_to_cm + inches_to_cm

print(height_in_cm)
