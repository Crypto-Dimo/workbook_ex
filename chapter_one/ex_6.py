meal_cost = float(input('How much did you pay for the meal?'))
tax = (meal_cost * 22) / 100
tip = (meal_cost * 18) / 100 
total = meal_cost + tax + tip
print(round(total, 2), '$')