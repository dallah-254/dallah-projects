import random
import string

def main():
     #Function to generate random password
     def generate_password(length):
         characters = string.ascii_letters + string.digits + string.punctuation
         password = ''.join(random.choice(characters) for i in range(length))
         return password
     
     length = int(input("Enter the desired password length: "))
     password = generate_password(length)
     print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

