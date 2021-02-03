feet = float(input('How many feet? '))

feet_to_inches = feet * 12
feet_to_yards = feet * 0.333333
feet_to_miles = feet * 0.000189394

print(feet, 'feet correspond to', feet_to_inches, 'inches')
print(feet, 'feet correspond to', feet_to_yards, 'yards')
print(feet, 'feet correspond to', round(feet_to_miles, 5), 'miles')
