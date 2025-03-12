# Create a list to store the number inputs
numbers = []
# Loop indefinitely to ask the user for a number
while True:
    # Prompt the user for input
    # Try to convert the input to an integer
    try:
        # If successful, add the number to the list and update the sum
        user_input = int(input("Enter a number: "))
    except ValueError:
        # Otherwise, break the loop if input is invalid
        break

# Check if there were valid inputs
# Calculate the average by dividing the sum by the number of elements in the list
# Print the average