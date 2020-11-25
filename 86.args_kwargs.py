# *args **kwargs both are variable so they can be anything but we always should use them as other developers use them

def super_func(name, *args, i='hi', **kwargs):
# Rule: params, *args, default parameters, **kwargs
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func('Patryk', 1,2,3,4,5, num1=5, num2=10))