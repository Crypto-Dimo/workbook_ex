a_plus = 4.0
a = 4.0
a_minus = 3.7
b_plus = 3.3
b = 3.0
b_minus = 2.7
c_plus = 2.3
c = 2.0
c_minus = 1.7
d_plus = 1.3
d = 1.0
f = 0

grade = input("Enter your grade: ")
grade = grade.lower()

grade_points = " "

if grade == "a+" or grade == "a":
    grade_points = a_plus
elif grade == "a-":
    grade_points = a_minus
elif grade == "b+":
    grade_points = b_plus
elif grade == "b":
    grade_points = b
elif grade == "b-":
    grade_points = b_minus
elif grade == "c+":
    grade_points = c_plus
elif grade == "c":
    grade_points = c
elif grade == "d+":
    grade_points = d_plus
elif grade == "d":
    grade_points = d
elif grade == "f":
    grade_points = f

if grade_points == " ":
    print("The grade entered is incorrect!")
else:
    print(f"The grade points corresponding to your grade are: {grade_points}.")
