# Ask the user to input 10 numbers
print("Enter 10 numbers")
numbers = []
seen = set()

for _ in range(10):
    num = int(input("Enter a number: "))

    # Only add the number if it hasn't been seen before
    if num not in seen:
        numbers.append(num)
        seen.add(num)

# Print the numbers while ignoring duplicate entries  
print("Numbers displayed with only their first occurrence:")
for num in numbers:
    print(num)