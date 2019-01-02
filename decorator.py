def my_decorator(tartget_function):
    def function_wrapper():
        return "Python is such a " + tartget_function() + " language!"
    return function_wrapper

@my_decorator
def tartget_function():
    return "cool"

tartget_function()