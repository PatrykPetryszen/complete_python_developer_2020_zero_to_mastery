from os import readlink


# With this method we don't need to close at the end

with open('test.txt', mode='r+') as my_file: #mode is for w - write (replaces everyting), r - read, r+ is for read/write, a - append
    text = my_file.write('hahaha?')
    print(my_file.readlines())
    

