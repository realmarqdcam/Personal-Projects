user_name = str(input('Enter your first name: '))

try:
    number = int(input('Enter your number of choice: '))
    print()
    print(f'Name: {user_name}  Number: {number}')
    print()

    if number > 0:
        print(f'Hello {user_name}! The number you entered, {number}, which is positive.')
    elif number < 0:
        print(f'Hello {user_name}! The number you entered, {number}, which is negative.')
    elif number == 0:
        print(f'Hello {user_name}! The number you entered was {number}.')

except ValueError:
    print('Invalid input has been entered. Exiting program.')