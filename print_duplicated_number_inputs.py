# Create an empty dictionary to store number inputs
number_inputs = {}
# Use a for loop to repeat the process 10 times
for i in range(10):
    # Prompt the user for a number
    user_input = int(input("Enter a number: "))
    # If the number exists in the dictionary, increment its count
    if user_input in number_inputs:
        number_inputs[user_input] += 1
    # Otherwise, add the number to the dictionary with a count of 1
    else:
        number_inputs[user_input] = 1

# Create an empty list to store duplicate numbers
# Iterate through the dictionary
#   - If a number appears more than once, add it to the list
# Print the list of numbers that were entered multiple times