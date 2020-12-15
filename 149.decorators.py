def hello():
    print('heeeellooooooo')

greet = hello
del hello

hello()

print(greet())