first_side = float(input("enter the measure of the triangle's fist side: "))
second_side = float(input("enter the measure of the triangle's second side: "))
third_side = float(input("enter the measure of the triangle's third side: "))

if first_side == second_side == third_side:
    tri_type = "equilateral"
elif first_side == second_side or first_side == third_side or second_side == third_side:
    tri_type = "isosceles"
else:
    tri_type = "scalene"

print(f"It's a {tri_type} triangle.")