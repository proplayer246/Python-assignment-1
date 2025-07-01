
# task1.py

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Division with error handling
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")
