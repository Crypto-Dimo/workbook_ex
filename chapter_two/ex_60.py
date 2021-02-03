year = int(input("Enter the year: "))

day_of_week = (year + ((year - 1) // 4) - ((year - 1) // 100) + ((year - 1) // 400)) % 7

if day_of_week == 0:
    day_name = "Sunday"
elif day_of_week == 1:
    day_name = "Monday"
elif day_of_week == 2:
    day_name = "Tuesday"
elif day_of_week == 3:
    day_name = "Wednesdy"
elif day_of_week == 4:
    day_name = "Thursday"
elif day_of_week == 5:
    day_name = "Friday"
elif day_of_week == 6:
    day_name = "Saturday"

print(f"In {year}, the first of january comes on {day_name}.")