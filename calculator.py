
def addition(a, b):

    #Performs addition of two numbers.

    result = a + b
    return result

def subtraction(a, b):

    #Performs subtraction of two numbers.


    result = a - b
    return result

def multiplication(a, b):

    #Performs multiplication of two numbers.


    result = a * b
    return result

def division(a, b):

    #Performs division of two numbers.

    if b == 0:
        return "Error: Cannot divide by zero."
    result = a / b
    return result

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"The result is: {addition(a, b)}")
        elif choice == '2':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"The result is: {subtraction(a, b)}")
        elif choice == '3':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"The result is: {multiplication(a, b)}")
        elif choice == '4':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"The result is: {division(a, b)}")
        elif choice == '5':
            print("Exiting the calculator...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()