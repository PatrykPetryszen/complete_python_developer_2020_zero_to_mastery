# dirty code

def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0: # Not else because we're giving a condition
        return False

# cleaner code

def is_even(num):
    return num % 2 == 0

print(is_even(50))