import math

with open("coefficients.txt", "r") as file:
    data = file.readline().split()
    a, b, c = map(float, data)

D = b**2 - 4*a*c

if D < 0:
    print("No real solutions (complex roots)")
elif D == 0:
    x = -b / (2*a)
    print(f"One real solution: x = {x}")
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Two real solutions: x1 = {x1}, x2 = {x2}
