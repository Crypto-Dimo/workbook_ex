days = int(input('number of days: '))
hours = int(input('number of hours: '))
minutes = int(input('number of minutes: '))
seconds = int(input('number of seconds: '))

seconds_in_day = 86400 * days
seconds_in_hour = 3600 * hours
seconds_in_minute = 60 * minutes

total_seconds = seconds_in_day + seconds_in_hour + seconds_in_minute + seconds

print('the total of seconds is: ', total_seconds, 'sec')
