import math

d = float(input('Height in meters: '))
Vi = 0
a = 9.8

Vf = math.sqrt(Vi ** 2 + 2 * a * d)

print('Thefinal spedd of the object is: ', Vf, 'm/s')