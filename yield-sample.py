def generate_squares(start, end):
    for num in range(start, end + 1):
        yield num * num  # Yield the square of each number

# Create the generator object
square_gen = generate_squares(1, 5)

# Iterate over the generator
for square in square_gen:
    print(square)  # Output: 1, 4, 9, 16, 25
