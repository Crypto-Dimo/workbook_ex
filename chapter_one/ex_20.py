# PV = nRT
# P = pressure in pascal
# V = volume in liters
# n = amount of substance in moles
# R = ideal gas constant = 8.314 = J/mol * K
# T = temperature

P = float(input('pressure: '))
V = float(input('volume: '))
T = float(input('temperature: '))
R = 8.314

n = P * V / R * T

print('The amount of substance in moles in: ', round(n, 2), 'moles')