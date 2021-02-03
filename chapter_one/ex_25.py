total_seconds = int(input('total seconds: '))

days = (total_seconds // 86400)
remainder_1 = int(total_seconds % 86400)

hours = (remainder_1 // 3600)
remainder_2 = int(remainder_1 % 3600)

minutes = (remainder_2 // 60)
seconds = int(remainder_2 % 60)

#old way
print('the date is: ', '%d:%02d:%02d:%02d.' % (days, minutes, hours, seconds))

#new way
print('the date is: ', '{:d}:{:02d}:{:02d}:{:02d}.' .format(days, minutes, hours, seconds))