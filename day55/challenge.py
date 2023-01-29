# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        res = func(*args)
        print(f"You called {function_name}{args}")
        print(f"It returned: {res}")

    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(x, y, z):
    return x + y + z


a_function(1, 2, 3)
