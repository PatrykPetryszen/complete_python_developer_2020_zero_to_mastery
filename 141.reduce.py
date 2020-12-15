from functools import reduce

my_list = [1,2,3]

def accumulato(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulato, my_list, 0))
print(my_list)

# Long story short reduce just adds all the values in the my_list
