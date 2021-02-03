import math

s1 = float(input('First triangle side: '))
s2 = float(input('Second triangle side: '))
s3 = float(input('Third triangle side: '))

s = (s1 + s2 + s3) / 2

area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print('the triangle area is: ', round(area, 2))