def my_decorator(func):
    def wrap_func(*args, **kwargs): # We use args to unpack positional arguments and kwargs for keywords arguments
        print('*********') #That way we can pass as many arguments as we want
        func(*args, **kwargs)
        print('*********')
    return wrap_func
#UP ^ Decorator Pattern

@my_decorator
def hello(greeting):
    print(greeting)

def bye():
    print('seee ya later')

hello('hiiii')