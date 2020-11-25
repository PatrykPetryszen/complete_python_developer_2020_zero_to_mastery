my_set = {1,2,3}
your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set)) # Only prints the set without updating it
# print(my_set)
#
# print(my_set.difference_update(your_set)) # Prints and updates the set
# print(my_set)
#
# my_set.discard(5)
# print(my_set)
#
# print(my_set.intersection(your_set))
print(my_set & your_set) # Same as intersection


print(my_set.isdisjoint(your_set)) # Do they have anything in common ? If they have gives False

print(my_set.union(your_set)) # Add sets together and remove the duplicates
print(my_set | your_set) # Same as union

new_set = {4,5}
your_new_set = {4,5,6,7,8,9,10}

print(new_set.issubset(your_new_set))
print(your_new_set.issuperset(new_set))