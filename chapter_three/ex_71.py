k = 4
x = 2
y = 3
z = 4

pi = 3 + (k / (x * y * z))
print(pi)

for i in range(0, 14):
    if i % 2 != 0:
        x += 2
        y += 2
        z += 2
        approx = (k / (x * y * z))
        pi = pi + approx
        print(pi)
    else:
        x += 2
        y += 2
        z += 2
        approx = - (k / (x * y * z))
        pi = pi + approx
        print(pi)




