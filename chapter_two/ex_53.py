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

grade_points = float(input("Enter your grade points, such as 4.0: "))

grade = " "

if grade_points > a_plus:
    grade = "A+"
elif 3.9 <= grade_points <= 4.0:
    grade = "A"
elif 3.6 <= grade_points <= 3.8:
    grade = "A-"
elif 3.2 <= grade_points <= 3.5:
    grade = "B+"
elif 2.9 <= grade_points <= 3.1:
    grade = "B"
elif 2.5 <= grade_points <= 2.8:
    grade = "B-"
elif 2.2 <= grade_points <= 2.5:
    grade = "C+"
elif 1.9 <= grade_points <= 2.1:
    grade = "C"
elif 1.5 <= grade_points <= 1.8:
    grade = "C-"
elif 1.2 <= grade_points <= 1.4:
    grade = "D+"
elif 1.0 <= grade_points <= 1.1:
    grade = "D+"
elif grade_points < 1.0:
    grade = "F"


if grade == " ":
    print("The grade entered is incorrect!")
else:
    print(f"The grade corresponding to your grade points is: {grade}.")
