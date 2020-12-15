
def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err: # If we want to se the eror we would need to f string instead of + err as it's built in exception in python
        print(f'please enter numbers {err}')

print(sum('1', 2))

def sum2(num3, num4):
    try:
        return num3/num4
    except (TypeError, ZeroDivisionError): # If we want to se the eror we would need to f string instead of + err as it's built in exception in python
        print('oooops')

print(sum2(1, 0))