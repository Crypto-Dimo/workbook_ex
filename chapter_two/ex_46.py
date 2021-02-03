
column = input("enter the column letter: ")
row = int(input("Enter the row number: "))

column = column.lower()

if column == 'a' or column == 'c' or column == 'e' or column == 'g':
    if row == 1 or row == 3 or row == 5 or row == 7:
        color = "black"
    if row == 2 or row == 4 or row == 6 or row == 8:
        color = "white"
 

if column == 'b' or column == 'd' or column == 'f' or column == 'h':
    if row == 1 or row == 3 or row == 5 or row == 7:
        color = "white"
    if row == 2 or row == 4 or row == 6 or row == 8:
        color = "black"

print(f"The square is {color}!")
