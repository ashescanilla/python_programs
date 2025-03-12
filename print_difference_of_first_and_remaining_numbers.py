# Ask for the first number
num1 = int(input("[1] Enter a number: "))

# Create a loop, and ask for a number each time, subtract that number to the first number
for i in range(2,11):
    num = int(input(f"[{i}] Enter a number: "))
    num1 -= num

# Print the modified first number after the loop ends
print(num1)