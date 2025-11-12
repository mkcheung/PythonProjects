def logging_decorator(function):
    def wrapper(*args):
        sumOfArgs = function(*args);
        print(f"You called {function.__name__}({args[0]},{args[1]},{args[2]})")
        print(f"It returned: {sumOfArgs}")
    return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)