dog_years = int(input("what's your dog's age? "))

if dog_years <= 2 and dog_years > 0:
    x = dog_years * 10.5
    print(f"The conversion in human years is: {x}")
elif dog_years > 2 and dog_years > 0:
    y = 21 + (dog_years - 2) * 7
    print(f"The conversion in human years is: {y}")
else:
    print("Wrong number, please enter a correct dog age.")