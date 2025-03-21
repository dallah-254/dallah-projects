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

def power(num1, num2):
    return math.pow(num1, num2)

def logarithm(num, base=math.e):
    if num > 0:
        return math.log(num, base)
    else:
        return "Error: Logarithm of a non-positive number is not defined"

def exponential(num):
    return math.exp(num)

def trigonometric_sin(num):
    return math.sin(num)

def trigonometric_cos(num):
    return math.cos(num)

def trigonometric_tan(num):
    return math.tan(num)

def factorial(num):
    if num >= 0 and num.is_integer():
        return math.factorial(int(num))
    else:
        return "Error: Factorial is not defined for negative numbers or non-integers"

def gcd(num1, num2,num3,num4,num5):
    return math.gcd(int(num1), int(num2), int(num3), int(num4), int(num5))

def absolute(num):
    return abs(num)

def rounding(num):
    return round(num)

def ceiling(num):
    return math.ceil(num)

def floor(num):
    return math.floor(num)

operations = {
    '1': ('Addition', addition),
    '2': ('Subtraction', subtraction),
    '3': ('Multiplication', multiplication),
    '4': ('Division', division),
    '5': ('Square', square),
    '6': ('Square Root', square_root),
    '7': ('Power', power),
    '8': ('Logarithm', logarithm),
    '9': ('Exponential', exponential),
    '10': ('Sine', trigonometric_sin),
    '11': ('Cosine', trigonometric_cos),
    '12': ('Tangent', trigonometric_tan),
    '13': ('Factorial', factorial),
    '14': ('Greatest Common Divisor', gcd),
    '15': ('Absolute Value', absolute),
    '16': ('Rounding', rounding),
    '17': ('Ceiling', ceiling),
    '18': ('Floor', floor)
}

def main():
    print("Choose an operation:")
    for key, value in operations.items():
        print(f"{key}: {value[0]}")

    choice = input("Enter the operation number: ")

    if choice in ['1', '2', '3', '4', '7']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = operations[choice][1](num1, num2)
    elif choice in ['5', '6', '9', '10', '11', '12', '13', '15', '16', '17', '18']:
        num = float(input("Enter the number: "))
        result = operations[choice][1](num)
    elif choice == '8':
        num = float(input("Enter the number: "))
        base = float(input("Enter the base (default is e): ") or math.e)
        result = operations[choice][1](num, base)
    elif choice == '14':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        num4 = float(input("Enter the fourth number: "))
        num5 = float(input("Enter the fifth number: "))
        result = operations[choice][1](num1, num2, num3, num4, num5)
    else:
        result = "Invalid operation number"

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
