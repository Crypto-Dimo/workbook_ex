T_celcius = float(input('Temperature in degrees celsius: '))

T_kelvin = T_celcius + 273.15
T_fahrenheit = T_celcius * (9 / 5) + 32

print(T_celcius, 'degrees celsius equal to', T_kelvin, 'degrees kelvin')
print(T_celcius, 'degrees celsius equal to', T_fahrenheit, 'degrees fahreinheit')