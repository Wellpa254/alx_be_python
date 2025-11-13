# Pattern Drawing with Nested Loops

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

# Draw the square pattern
while row < size:
    # Draw one row using a for loop
    for col in range(size):
        print("*", end="")  # Print stars on the same line
    print()  # Move to the next line after finishing a row
    row += 1
