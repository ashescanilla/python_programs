# Set to store unique numbers
numbers = set()

while True:
    try:
    # Ask user for a number
    num = int(input("Enter a number: "))

    # Check if the number is unique or a duplicate
    # Exit the loop if an invalid input is entered