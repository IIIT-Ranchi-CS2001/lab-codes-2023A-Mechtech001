# Roots of Quadratic Equation

import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
   
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The equation has two distinct real roots: Root1 = ",root1, "and Root2 = ",root2)
elif discriminant == 0:
    # One real repeated root
    root = -b / (2 * a)
    print("The equation has one real repeated root: Root1 = Root2 = ",root)
else:
    # Two complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    print("The equation has two complex roots: Root1 = ",real_part, " + ",imaginary_part, "i and Root2 = ",real_part, " - ", imaginary_part,"i")