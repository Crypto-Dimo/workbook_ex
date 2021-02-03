print('latitude (t1, g1)')
print('longitude (t2, g2)')

import math

t1 = float(input('What is the latitude t1 value? '))
g1 = float(input('What is the longitude g1 value? '))
t2 = float(input('What is the latitude t2 value? '))
g2 = float(input('What is the longitude g2 value? '))

distance = 6371.01 * arccos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print(float(distance))