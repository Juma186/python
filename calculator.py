
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


# Display menu
print("Select input")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice(1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(num1, "+", num2, "=", addition(num1, num2))

            elif choice == "2":
                print(num1, "-", num2, "=", subtraction(num1, num2))

            elif choice == "3":
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == "4":
                print(num1, "/", num2, "=", divide(num1, num2))

        except ValueError:
            print("Invalid input! Please enter numeric values.")

    else:
        print("Invalid choice! Please select a valid option.")