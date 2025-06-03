# WAP to calculate area of triangle and rectangle.
# area of triangle = 0.5 * (base * height)
# area of rectangle = length * breadth

base = int(input("Enter base for triangle: "))
height = int(input("Enter height for triangle: "))

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))

tri_area = 0.5 * (base * height)
print("Area of triangle = ", tri_area)

rect_area = length * breadth
print("Area of retangle = ", rect_area) 