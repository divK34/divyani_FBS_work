# 6. WAP to input two angles from user and find third angle of the triangle. Formula := a + b + c = 180 degree
# 9. WAP to enter base and height of a triangle and find its area. Formula := area = 1/2 * base * height(perpendicular angle)
# 10. WAP to calculate area of an equilateral triangle. Formula := area = (sqrt(3)/4) * side (single side/face)

a = int(input("Enter angle A of the triangle = "))
b = int(input("Enter angle B of the triangle = "))
c = 180 - (a + b)

base = 18
height = 22
tri_area = 0.5 * base * height 

a_side = 5
equ_tri_area = ((3 ** 0.5) / 4) * (a_side ** 2)

print("Third angle of triangle is = ",c)
print("Area of triangle is = ",tri_area)
print("Area of equilateral triangle is = ",equ_tri_area)





