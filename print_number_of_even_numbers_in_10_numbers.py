# Create a variable to store the number of even number inputs and set its value to 0
even_count = 0

# Create a for loop to ask the user for 10 number inputs
for i in range(10):
    num = int(input("Enter a number: "))
    # Inside the loop, check if the number is even by using the modulus operator (%)
    if num % 2 == 0:
        # If the number is even, increment the counter variable by 1
        even_count += 1

# After the loop, print the counter variable