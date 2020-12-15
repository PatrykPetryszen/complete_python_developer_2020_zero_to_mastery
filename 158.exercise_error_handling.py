
while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break # because we are breaking out of the loop we won't reach print at the bottom
    else:
        print('thank you!')
    finally: # It works every time regardles of error and exceptions
        print('ok, I am finally done') 
    print('can you hear me ?')