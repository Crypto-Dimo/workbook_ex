kPa = float(input('Pressure in kilopascal: '))

PSI = kPa / 6.89475729
mmHg = kPa * 7.50062
atm = kPa * 0.0098692326671601

print(kPa, 'kilopascals equals to', round(PSI, 4), 'PSI')
print(kPa, 'kilopascals equals to', round(mmHg, 4), 'mmHg')
print(kPa, 'kilopascals equals to', round(atm, 4), 'atm')