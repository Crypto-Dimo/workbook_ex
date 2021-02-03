rating = float(input("Enter your rating: "))

performance = " "
wage_increase = " "

if rating == 0.0:
    performance = "unacceptable"
    wage_increase = 2400 * rating
elif rating == 0.4:
    performance = "acceptable"
    wage_increase = 2400 * rating
elif rating >= 0.6:
    performance = "meritorius"
    wage_increase = 2400 * rating


if performance != " ":
    print(f"Your performance was {performance} and your wage increase corresponds to ${wage_increase}.")
else:
    print("Invalid rating.")