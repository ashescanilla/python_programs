# Ask for 2 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Identify the start of the range with min() method plus 1 to exclude the inputted number
start = min(num1, num2) + 1
# Identify the end of the range with max() method
end = max(num1, num2)

# Print the range of numbers
print(*range(start, end))