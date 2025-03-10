# Create a loop with an end of 101
for i in range(101):
    # Check if the iteration doesn't end with zero by using the modulo operator (%) and divisor of 10
    if i % 10 != 0:
        # If is doesn't end with zero, print the iteration
        print(i)