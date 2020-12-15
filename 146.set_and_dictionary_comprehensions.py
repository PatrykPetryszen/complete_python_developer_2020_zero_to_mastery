# list, set, dictionary
# reminder: sets don't allow duplicates

my_list = {char for char in 'hello'} # Create a variable char and for each iterable add it to the list

my_list2 = [x for x in range(0,100)]

my_list3 = [num**2 for num in range(0,100)]

my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k:v**2 for k,v in simple_dict.items() if v%2==0}
print(my_dict)

my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)