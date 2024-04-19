def fibonacci_generator():
    a = 0
    b = 1

    def next_value():
        nonlocal a, b
        yield a  # Yield the current value of 'a' (next Fibonacci number)
        new_a = b
        new_b = a + b
        a = new_a
        b = new_b

    return next_value

# Create the generator object
fib_gen = fibonacci_generator()

# Iterate over the generator
for i in range(10):
    print(next(fib_gen))  # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
