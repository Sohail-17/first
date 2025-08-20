num1 = float(input('Enter the first number'))
num2 = float(input('Enter the next number'))
operation = input('Enter the operation you want to perform')
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print(f'Division is invalid as the 2nd number is {num2}')
    else:
        result = num1 / num2
else:
    print('Invalid operation entered')
print(f'The result opf your operation is {result}')     
                                                                          