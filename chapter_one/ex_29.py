# Ta = air temperature in degrees celsius
# V = wind speed in km/h

Ta = float(input('Waht is the air temperature? '))
V = float(input('What is the wind speed? '))

if Ta <= 10 and V >= 4.8:
    WCI = 13.12 + 0.6215 * Ta - 11.37 * (V ** 0.16) + 0.3965 * Ta * (V ** 0.16)
    print('The Wind Chill Index is', int(WCI))
else:
    print('The WCI cannot be calculated sice the air temperature is higher than 10 degrees celcius or the wind speed is less than 4.8 km/h')