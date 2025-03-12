# Ask the user to input 10 numbers
print("Enter 10 numbers")
numbers = []
seen = set()

for _ in range(10):
    num = int(input("Enter a number: "))
    
# Add the number only if it hasn't been entered previously
# Print the numbers while ignoring duplicate entries  