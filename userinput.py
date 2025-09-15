import math

def solve_quadratic(a, b, c):
    print(f"Equation: {a}x^2 + {b}x + {c} = 0")
    d = b**2 - 4*a*c
    if d < 0:
        print("No real roots (complex solution).")
    elif d == 0:
        x = -b / (2*a)
        print(f"One real root: x = {x}")
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Two real roots: x1 = {x1}, x2 = {x2}")

# Option 1: User input
choice = input("Enter coefficients manually (Y/N)? ")

if choice.lower() == "y":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    solve_quadratic(a, b, c)

else:
    # Option 2: Read from file
    with open("coefficients.txt", "r") as f:
        values = f.read().split()
        a, b, c = map(float, values)
        solve_quadratic(a, b, c)
