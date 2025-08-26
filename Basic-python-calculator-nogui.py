num1 = float(input("Enter the first number "))
num2 = float(input("Enter the next number "))
operation = input("Enter the operation you want to perform ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print(f"Division is invalid as the 2nd number is {num2}")
        result = "Your head man! The divisor is zero how can you divide with 0?"
    else:
        result = num1 / num2
else:
    print("Invalid operation entered")
    result = "What man! You have to select from +, -, /, * only man idiot!"
print(f"The result of your operation is {result} ")
print("Press ctrl + F5 to restart the program!")     