# Prompt the user for numbers until an invalid entry is detected, then show the minimum value.

print("Enter numbers (input anything non-numeric to stop)")

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break  # Exit the loop when an invalid input is entered

# Print the lowest number if a valid entry has been recorded.
if numbers:
    print("The lowest number entered is:", min(numbers))
else:
    print("No valid numbers were entered.")