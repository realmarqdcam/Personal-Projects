try:
    temperature = int(input("Enter temperature in Celsius: "))
    fahrenheit = temperature * 1.8 + 32
    print(f'{temperature} degrees Celsius is {fahrenheit} degrees Fahrenheit!')
except ValueError:
    print('Invalid input! Please enter a numeric value for temperature.')