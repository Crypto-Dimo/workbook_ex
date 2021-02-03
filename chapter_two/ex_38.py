sides = int(input("How many sides your shape has? "))

name = " "
if sides == 3:
    name = "triangle"
elif sides == 4:
    name = "square"
elif sides == 5:
    name = "pentagon"
elif sides == 6:
    name = "hexagon"
elif sides == 7:
    name = "heptagon"
elif sides == 8:
    name = "octagon"
elif sides == 9:
    name = "nonagon"
elif sides == 10:
    name = "decagon"

if name == " ":
    print("Error, invalid value!")
else:
    print(f"That's a {name}.")
