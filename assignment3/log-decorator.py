# Task 1: Writing and Testing a Decorator

import logging

# set up logger
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

# accept function
def logger_decorator(func):
    # accept arguments passed to function
    def wrapper(*args, **kwargs):
        # execute function, assign return value
        result = func(*args, **kwargs)

        # create list of positional params if passed, or "none"
        pos_params = list(args) if args else "none"

        # create dict of keyword params if passed, or "none"
        kw_params = kwargs if kwargs else "none"

        # construct and write log entry
        logger.log(logging.INFO,
            f"function: {func.__name__}\n"
            f"positional parameters: {pos_params}\n"
            f"keyword parameters: {kw_params}\n"
            f"return: {result}\n"
        )

        return result
    return wrapper

@logger_decorator
def greeting():
    print("Hello, World!")

@logger_decorator
# define function that takes positional arguments, return bool
def birthdate(*args):
    return True

@logger_decorator
# define function that takes keyword argument, return function obj
def user(**kwargs):
    return logger_decorator

greeting()
birthdate(8, 19, "nineteen ninety-one")
user(user="Gianni", role="developer")