my_set = {1,2,3,4,5,5}

print(my_set) # In sets there are no duplicates so we won't have second 5 when printing the output

my_set.add(100)
my_set.add(2) # won't be added as we already have 2

print(my_set)

my_list = [1,2,3,4,5,5]

print(set(my_list)) # We're converting list to set