def addition(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

choice = input("enter operation to be performed: ")

if choice == "add":
    result = addition(num1, num2)
elif choice == "sub":
    result = subtraction(num1, num2)
elif choice == "mult":
    result = multiply(num1, num2)
elif choice == "div":
    result = divide(num1, num2)
else:
    result = "Invalid choice"

print("result: ", result)
