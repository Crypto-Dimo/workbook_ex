year = int(input("Enter the year: "))

if year % 12 == 8:
    animal = "dragon"
elif year % 12 == 9:
    animal = "snake"
elif year % 12 == 10:
    animal = "horse"
elif year % 12 == 11:
    animal = "sheep"
elif year % 12 == 0:
    animal = "monkey"
elif year % 12 == 1:
    animal = "rooster"
elif year % 12 == 2:
    animal = "dog"
elif year % 12 == 3:
    animal = "pig"
elif year % 12 == 4:
    animal = "rat"
elif year % 12 == 5:
    animal = "ox"
elif year % 12 == 6:
    animal = "tiger"
elif year % 12 == 7:
    animal = "hare"

print(f"{year} is the year of the {animal}.")