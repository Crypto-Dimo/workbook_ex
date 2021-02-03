spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
autumn = ['september', 'october', 'november']
winter = ['december', 'january', 'february']

day = int(input("Enter the day: "))
month = input("Enter the month: ")

season = " "
message = " "

if month in spring:
    season = "spring"
    if month == spring[0] and 1 < day < 20:
        season = "winter"
    elif month == spring[0] and day == 20:
        message = "first day of spring!"
elif month in summer:
    season = "summer"
    if month == summer[0] and 1 < day < 21:
        season = "spring"
    elif month == summer[0] and day == 21:
        message = "first day of summer!"
elif month in autumn:
    season = "autumn"
    if month == autumn[0] and 1 < day < 22:
        season = "summer"
    elif month == autumn[0] and day == 22:
        message = "first day of autumn!"
elif month in winter:
    season = "winter"
    if month == winter[0] and 1 < day < 21:
        season = "autumn"
    elif month == winter[0] and day == 21:
        message = "first day of winter!"

if message == " ":
    print (f"We are in {season}.")
else:
    print(f"Today is the {message}")