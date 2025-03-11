# Ask for 2 number inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the second number is not equal to 0
if num2 != 0:
    # Calculate the remainder of the two numbers using the modulus operator (%)
    remainder = num1 % num2
    # Print the remainder