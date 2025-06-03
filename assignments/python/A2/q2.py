# Convert temp from Celsius to Fahrenheit. 
# Formula := C/5 = (F-32)/9 
# F = (9/5 x C) + 32

celsius = int(input("Enter temperature in Celsius: "))

fahrenheit = ((9/5) * celsius) + 32

print(celsius,"C =",fahrenheit,"F")