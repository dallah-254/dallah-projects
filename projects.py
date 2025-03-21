import math

operations = ['addition', 'subtraction', 'division', 'multiplication', 'square', 'square_root']

print("Choose an operation:")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
for item in operations:
    
    if item == 'addition':
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    elif item == 'subtraction':
        result = num1 - num2
        print(f"The difference between {num1} and {num2} is {result}")
    elif item == 'division':
        result = num1 / num2
        print(f"The quotient of {num1} divided by {num2} is {result}")
    elif item == 'multiplication':
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}")
    elif item == 'square':
        num3 = float(input("Enter a number: "))
        result = num3 ** 2
        print(f"The square of {num3} is {result}")
    elif item == 'square_root':
        num4 = float(input("Enter a positive number: "))
        if num4 < 0:
            print("Square root of a negative number is not defined.")
        else:
            result = math.sqrt(num4)
            print(f"The square root of {num4} is {result}")