# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle
# Equilateral = All sides are equal
# Isosceles = Two sides are equal
# Scalene = No sides are equal

a = int(input("Enter side one: "))
b = int(input("Enter side two: "))
c = int(input("Enter side three: "))

if a == b == c:
    print("It is an Equilateral triangle")
elif (a == b != c) or (a == c != b) or (b == c != a):
    print("It is an Isosceles triangle")
else:
    print("It is a Scalene triangle")