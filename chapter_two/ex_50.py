magnitude = float(input("Enter the magnitude: "))

if magnitude < 2.0:
    descriptor = "micro"
elif 2.0 <= magnitude < 3.0:
    descriptor = "very minor"
elif 3.0 <= magnitude < 4.0:
    descriptor = "minor"
elif 4.0 <= magnitude < 5.0:
    descriptor = "light"
elif 5.0 <= magnitude < 6.0:
    descriptor = "moderate"
elif 6.0 <= magnitude < 7.0:
    descriptor = "strong"
elif 7.0 <= magnitude < 8.0:
    descriptor = "major"
elif 8.0 <= magnitude < 10.0:
    descriptor = "great"
elif magnitude > 10.0:
    descriptor = "meteoric"

print(f"A magnitude {magnitude} earthquake is considered to be a {descriptor} earthquake.")