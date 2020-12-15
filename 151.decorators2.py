# Decorator is simply a function that wraps another functions and enhances it (changes it )

def my_decorator(func):
    def wrap_function():
        print('******')
        func()
        print('******')
    return wrap_function

@my_decorator
def hello():
    print('heelllo')

@my_decorator
def bye():
    print('see ya later')

bye()

hello2 = my_decorator(hello)
hello2()