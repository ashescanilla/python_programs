# Create an empty dictionary to store the number and its input count
numbers = {}
# Using a while True loop
while True:
    # Try asking the user for a number and convert it into an integer
    try:
        number = int(input("Enter a number: "))
        # If the user enters a valid integer value
        # Check if the number exists in the dictionary
        # If the number exists increase its input count by 1, 
        # otherwise add the number to the dictionary with an input count of 1
    # If the user enters an invalid integer value,
    except ValueError:
        # break out of the while loop
        break
    
# Create a variable to store the number with the highest input count, and set its current value to "None"
# Iterate through the dictionary and identify the number with the highest input count
# Check if there were any valid inputs by checking if the variable is not "None"
# Print the variable