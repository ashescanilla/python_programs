# Set to store unique numbers
numbers = set()

while True:
    try:
        # Ask user for a number
        num = int(input("Enter a number: "))

        # Identify if the number is unique or a duplicate
        if num in numbers: 
            print("Duplicate") 
        else: 
            print("Unique") 
            numbers.add(num) 

    except ValueError:
        # Exit the loop if an invalid input is entered
        print("Invalid input. Exiting.")
        break