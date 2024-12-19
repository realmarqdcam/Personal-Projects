name = input('Enter your name: ')
age = int(input('Enter your age, as of today: '))
major = input('Enter your current major: ')
friends = int(input('Enter your amount of friends: '))
height = input('Enter your current height in feet and inches (e.g., 5.9 for 5\'9"): ')

# Split the height into feet and inches using the decimal point
height_parts = height.split('.')
feet = int(height_parts[0])
inches = int(height_parts[1]) if len(height_parts) > 1 else 0

print()
print(f"{name} is {age}, is {feet} feet and {inches} inches tall and currently studies {major}; they have {friends} friends at their university!")