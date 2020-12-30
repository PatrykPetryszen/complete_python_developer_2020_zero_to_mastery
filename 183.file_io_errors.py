try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err: #IOError refers to the machine having troubles to do some IO operation
    print('IO error')
    raise err
