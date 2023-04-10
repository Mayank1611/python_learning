num1 = float(input("enter the first number: "))
op = input("enter operator: ")
num2 = 5

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid command")
