def log_function(function):
    
    def wrapper(*args, **kwargs):
        print(f"Calling function: {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Function returned: {result}")
        return result
    return wrapper

@log_function
def my_function(x, y):
    return x + y

my_function(5, 3)  # Output:
                    # Calling function: my_function
                    # Function returned: 8
