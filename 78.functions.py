def say_hello(): # In order to take an action on the function we need to use () at the end and also when we call a function we use ()
    print('helllooooo')

say_hello()

def show_tree():
    fill = '*'
    empty = ' '
    for row in picture:
        for pixel in row:
            if (pixel):  # We don't need pixel == 1 as pixel itself is a TRUE value
                print(fill, end='')  # We use end to don't go to new line \n
            else:
                print(empty, end='')  # We use end to don't go to new line \n
        print('\n')

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


show_tree()
show_tree()