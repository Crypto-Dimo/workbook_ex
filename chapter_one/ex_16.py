import math

r = float(input('What\'s the radius? '))

area = math.pi * (r ** 2)
volume = 4 / 3 * math.pi * (r ** 3)

print('The area of the circle is: ', round(area, 2))
print('The volume of the sphere is: ', round(volume, 2))