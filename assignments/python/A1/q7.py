# 7. WAP to Find the Roots of a Quadratic Equation.
# formula := x = b+sqrt((b^2-4ac)/2a) and y = b-sqrt((b^2-4ac)/2a) 

a = 1
b = 4
c = 3

inner_sqrt_calc = (b**2 - (4*a*c)) / (2*a)    # (9 - 32)/4 
sqrt_calc = inner_sqrt_calc ** 0.5            # sqr_root formula is num^0.5    

x = b + sqrt_calc
y = b - sqrt_calc

print("Points of Quadratic equation are: ")
print("x =",x,"and y =",y)