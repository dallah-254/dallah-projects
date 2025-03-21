import math

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def square(num):
    return num ** 2

def square_root(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        return "Error: Square root of a negative number is not defined"

operations = {
    '1': ('Addition', addition),
    '2': ('Subtraction', subtraction),
    '3': ('Multiplication', multiplication),
    '4': ('Division', division),
    '5': ('Square', square),
    '6': ('Square Root', square_root),
}
print(operations)

def main():
    print("Choose an operation:")
    for key, value in operations.items():
        print(f"{key}: {value[0]}")

    choice = input("Enter the operation number: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = operations[choice][1](num1, num2)
    elif choice == '5':
        num = float(input("Enter a number: "))
        result = square(num)
    elif choice == '6':
        num = float(input("Enter a positive number: "))
        result = square_root(num)
    else:
        result = "Invalid operation number"

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
