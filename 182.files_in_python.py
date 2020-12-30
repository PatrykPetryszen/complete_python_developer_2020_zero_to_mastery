my_file = open('test.txt')

print(my_file.read())
my_file.seek(0) #Moves the cursor to the beginning
print(my_file.read())
my_file.seek(0)
print(my_file.read())
print(my_file.readline())

my_file.close() # We always should close the open once we're done