# Initialize an empty list to store user input
numbers = []

# Ask the user to input 10 numbers
print("Enter 10 numbers:")
for _ in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Initialize a dictionary to track how many times each number appears
frequency_count = {}

# Record the frequency of each number in the list
# Display numbers that appear only once