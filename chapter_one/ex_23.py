import math

s = float(input('side of the polygon: '))
n = int(input('number of sides: '))

area = n * (s ** 2) / 4 * math.tan(math.pi / n)

print('the area of the polygon is: ', round(area, 2))
