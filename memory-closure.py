def outer_function(initial_value):

    print("Entre a counter...")
  
    count = initial_value

    def inner_function():
        nonlocal count  # Mark count as nonlocal to modify it
        count += 1
        return count

    return inner_function  # Closure is created here


counter = outer_function(5)  # Call outer function and assign the returned inner function

# Calling counter multiple times (the closure) modifies the captured count from outer_function
print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3
