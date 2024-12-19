try:
    operation = str(input('Enter a mathematical operation (ex. +, -, *, /, or %): '))


    if operation not in ['+', '-', '*', '/', '%']:
        raise ValueError('Invalid operation!')

    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter your second number: '))


    if (operation == '/' or operation == '%') and number2 == 0:
        raise ValueError('Cannot divide by zero!')

    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        result = round(number1 / number2, 2)
    elif operation == '%':
        result = number1 % number2

    print(f'For the given operation, {operation}, the result is: {result}')

except ValueError as e:
    if str(e):
        print(str(e))
    else:
        print('Invalid user input!')