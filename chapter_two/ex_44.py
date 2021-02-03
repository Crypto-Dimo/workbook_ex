one_usd = "George Washington"
two_usd = "Thomas Jefferson"
five_usd = "Abraham Lincoln"
ten_usd = "Alexander Hamilton"
twenty_usd = "Andrew Jackson"
fifty_usd = "Ulysses S. Grant"
hundred_usd = "Benjamin Franklin"

banknote = int(input("Enter the banknote denomination, such as 5 for $5 dollar banknote: "))

name = " "

if banknote == 1:
    name = one_usd
elif banknote == 2:
    name = two_usd
elif banknote == 5:
    name = five_usd
elif banknote == 10:
    name = ten_usd
elif banknote == 20:
    name = twenty_usd
elif banknote == 50:
    name = fifty_usd
elif banknote == 100:
    name = hundred_usd

if name == " ":
    print("Invalid banknote!")
else:
    print(f"The face on the banknote represents {name}.")