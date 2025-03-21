import math

numbers = []

def input_numbers():
    print("Enter a number or type 'stop' to stop:")
    while True:
        number = input()
        if number == 'stop':
            print("Numbers entered:", numbers)
            print("entry complete")
            break
        try:
            number = float(number)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or type 'stop' to stop.")
operations = ['add', 'subtract', 'multiply', 'divide']

def perform_operation(add, subtract, multiply, divide):
    def add():
        return sum(numbers)
    print(f"Result of adding {numbers} is {add()}")


    def subtract():
        return numbers[0] - sum(numbers[1:])
    print(f"Result of subtracting {numbers} is {subtract()}")


    def subtract_from_the_largest():
        return max(numbers) - sum(numbers)
    print(f"Result of subtracting {numbers} from the largest number is {subtract_from_the_largest()}")


    def multiply():
        return math.prod(numbers)
    print(f"Result of multiplying {numbers} is {multiply()}")


    def divide():
        result = numbers[0]
        for number in numbers[1:]:
            result /= number
        return result
    print(f"Result of dividing {numbers} is {divide()}")
    
def main():
    input_numbers()
    if len(numbers) < 2:
        print("enter two numbers or more")
    elif(len(numbers) >= 2):
        perform_operation('add', 'subtract', 'multiply', 'divide')
    else:
        print("Invalid input. Please enter a number or type 'stop' to stop.")

main()


