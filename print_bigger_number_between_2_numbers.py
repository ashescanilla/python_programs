# Ask for 2 number inputs

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the 2 numbers
bigger_number = None
if num1 > num2:
    bigger_number = num1
elif num2 > num1:
    bigger_number = num2

# Print the bigger number