import random

red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)

spin = random.randint(0, 37)

if spin in red:
    reward_color = "Pay Red"
else:
    reward_color = "Pay Black"

if spin % 2 == 0:
    reward_even = "Pay Even"
else:
    reward_even = "pay Odd"

if spin in range(1, 18):
    reward_range = "Pay 1 to 18"
else:
    reward_range = "Pay 18 to 36"

if spin == 37:
    print("Pay 00")
elif spin == 0:
    print("Pay 0")
else:
    print(f"The spin resulted in {spin}")
    print(f"Pay {spin}")
    print(reward_color)
    print(reward_even)
    print(reward_range)