new_y_day = ["january", 1]
canada_day = ["july", 1]
christmas_day = ["december", 25]


month = input("enter the month's name: ")
day = int(input("enter the day: "))
month = month.lower()

if month == new_y_day[0] and day == new_y_day[1]:
    holiday = "New Year's Eve"
elif month == canada_day[0] and day == canada_day[1]:
    holiday = "Canada Day"
elif month == christmas_day[0] and day == christmas_day[1]:
    holiday = "Christmas Day"

print(f"It's {holiday}!")