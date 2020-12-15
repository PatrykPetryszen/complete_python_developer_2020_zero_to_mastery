# Error Handling

while True:
    try: # Try this
        age = int(input('what is your age?'))
        print(age)
    except ValueError: # If there is an error do this
        print('please enter a number')
    except ZeroDivisionError: # If there is another type of error do this
        print('please enter age higher than 0')
    else: # If there is no error do this
        print(f'You are {age} years old')
        break