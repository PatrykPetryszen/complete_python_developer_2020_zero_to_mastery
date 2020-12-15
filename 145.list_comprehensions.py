# list, set, dictionary

# my_list = [char for char in iterable]

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# Same thing as :

my_list = [char for char in 'hello'] # Create a variable char and for each iterable add it to the list

my_list2 = [x for x in range(0,100)]
print(my_list2)

my_list3 = [num**2 for num in range(0,100)]

my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
print(my_list4)