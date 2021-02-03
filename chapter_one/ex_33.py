first_num = int(input('First number: '))
second_num = int(input('Second number: '))
third_num = int(input('Third number: '))

smallest = min(first_num, second_num, third_num)
largest = max(first_num, second_num, third_num)
middle = (first_num + second_num + third_num) - (smallest + largest)

print('Sorted from smallest to largest:', smallest, middle,largest)
