month = input("Enter the month name: ")
month = month.lower()

days = 31 

if month == "april" or month == "june" or month == "september" or month == "november":
    days = 30
elif month == 'february':
    days = "28 or 29"

print(f"{month.title()} has {days} days in it.")