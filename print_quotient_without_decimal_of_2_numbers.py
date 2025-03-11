# Ask for 2 number inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the second input is not zero
if num2 != 0:
    # Floor divide the two numbers using (//) operator
    result = num1 // num2
    # Print the result
    print(result)