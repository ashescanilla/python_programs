# Create an empty dictionary to store the number and its input count
numbers = {}
# Using a while True loop
while True:
    # Try asking the user for a number and convert it into an integer
    # If the user enters a valid integer value
    try:
        number = int(input("Enter a number: "))
        # Check if the number exists in the dictionary
        if number in numbers:
            # If the number exists increase its input count by 1, 
            numbers[number] += 1
        else:
            # otherwise add the number to the dictionary with an input count of 1
            numbers[number] = 1

    # If the user enters an invalid integer value,
    except ValueError:
        # break out of the while loop
        break

# Create a variable to store the number with the highest input count, and set its current value to "None"
number_with_highes_input_count = None
# Iterate through the dictionary and identify the number with the highest input count
for number, count in numbers.items():
    if number_with_highes_input_count is None or count > numbers[number_with_highes_input_count]:
        number_with_highes_input_count = number

# Check if there were any valid inputs by checking if the variable is not "None"
if number_with_highes_input_count is not None:
    # Print the variable
    print(f"The number with the highest input count is {number_with_highes_input_count}")