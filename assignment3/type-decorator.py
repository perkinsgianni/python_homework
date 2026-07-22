# Task 2: A Decorator that Takes an Argument

# decorator factory, accept argument and return decorator
def type_converter(type_of_output):
    # accept function
    def type_decorator(func):
        # accept arguments passed to function
        def wrapper(*args, **kwargs):
            # execute function, assign return value
            x = func(*args, **kwargs)
            # convert type
            return type_of_output(x)
        return wrapper
    return type_decorator


@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

# confirm return value of return_int() is str
y = return_int()
print(type(y).__name__)

# try conversion of return_string() to int
try:
   y = return_string()
   print("shouldn't get here!")
# execute when type conversion fails
except ValueError:
   print("can't convert that string to an integer!")