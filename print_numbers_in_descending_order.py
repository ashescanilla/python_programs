# Continuously prompt the user for numeric input until an invalid entry is detected.
print("Enter numbers (input anything non-numeric to stop)")

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break  # Stop taking input on invalid entry

# Print the numbers in descending order if there is at least one valid entry.
if numbers:
    print("Numbers entered (highest to lowest):", numbers.sort(reverse=True))