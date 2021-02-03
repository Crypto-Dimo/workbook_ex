year = int(input("Enter the year: "))

if (year % 400 == 0):
    is_leap_year = True
elif (year % 100 == 0):
    is_leap_year = False
elif (year % 4 == 0):
    is_leap_year = True
else:
    is_leap_year = False

month = int(input("Enter the month: "))

if month in (1, 3, 5 , 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if is_leap_year:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30

day = int(input("Enter the day: "))

if day < month_length:
    day += 1
else:
    day = 1

if month == 12:
    month = 1
    year += 1
else:
    month += 1

print(f"Based on the date entered, the next day will be: {day:02d}/{month:02d}/{year}")


if is_leap_year:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")