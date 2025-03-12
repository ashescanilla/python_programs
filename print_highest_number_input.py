# Create a variable to store the highest number
highest_number = None
# Create an infinite loop with a while True statement
while True:
    # Inside the loop, ask the user for a number input
    try:
        # Convert the input to an integer
        user_input = int(input("Enter a number: "))
    # If successful, check if the input is greater than the stored highest number
    # If yes, update the highest number
    except ValueError:
        # If input is invalid (non a number), break out of the loop
        break
    
# Print the highest number