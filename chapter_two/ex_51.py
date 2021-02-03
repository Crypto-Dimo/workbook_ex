import cmath

a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))
c = float(input("Enter the value of 'c': "))

discriminant = (b ** 2) - (4 * a * c)

sol_1 = " "
sol_2 = " "

if discriminant < 0:
   sol_1 = " "
   sol_2 = " " 
   print("There are no real roots.")
elif discriminant == 0 or discriminant > 0:
    sol_1 = (-b-cmath.sqrt(discriminant))/(2*a)
    sol_2 = (-b+cmath.sqrt(discriminant))/(2*a)

print(sol_1)
print(sol_2)


