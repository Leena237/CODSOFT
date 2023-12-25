def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    operations = {
        '+': addition,
        '-': subtraction,
        '*': multiplication,
        '/': division
    }

    while True:
        X = float(input("Enter first number: "))
        Y = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        if operation in operations:
            result = operations[operation](X, Y)
            print(f"Result: {result}")
        else:
            print("Invalid operation !! Please enter +, -, *, or /.")

        Next_Calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if Next_Calculation != 'yes':
            break

if __name__ == "__main__":
    calculator()
