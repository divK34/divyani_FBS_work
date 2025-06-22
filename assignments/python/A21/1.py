# 1. Develop a simple calculator program that performs basic arithmetic operations (+, -, *, /) on two numbers provided by the user. The program should ask the user for the numbers and the operator. However, the program should handle the following exceptions: 
    # a. Invalid Number: If the user enters a number that is not valid, catch the exception and display an error message. 
    # b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or "/", catch the exception and display an error message. 
    # c. Division by Zero: If the user tries to divide by zero, catch the exception and display an error message. 
# Write a program that performs the requested arithmetic operation and handles the exceptions as described above.

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        
        num2 = float(input("Enter the second number: "))
    
        operator = input("Enter an operator (+, -, *, /): ")

        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operator")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2

        print("Result =", result)

    except ValueError as ve:
        print("Exception =", ve)
    except ZeroDivisionError as zde:
        print("Exception =", zde)

calculator()
