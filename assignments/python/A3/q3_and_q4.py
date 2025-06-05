# WAP to input angles of a triangle and check whether triangle is valid or not
# -> A triangle is valid if sum of all three angles is equal to 180
# WAP to input all sides of a triangle and check whether triangle is valid or not
# -> A triangle is valid if the sum of its two sides is greater than the third side.

aa = int(input("Enter an angle of the triangle: "))
ba = int(input("Enter an angle of the triangle: "))
ca = int(input("Enter an angle of the triangle: "))

sum_of_angles = aa + ba + ca

if sum_of_angles == 180:
    print("It is a valid triangle")
else:
    print("It is unvalid triangle")

d = int(input("Enter a side of the triangle: "))
e = int(input("Enter a side of the triangle: "))
f = int(input("Enter a side of the triangle: "))

if (d + e > f) or (d + f > e) or (e + f > d):
    print("it is a valid triangle")
else:
    print("it is unvalid triangle")