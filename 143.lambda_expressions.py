# We use lambda expressions when we have a function but we need to use it once
# So lambda is one time anynomyous function. Additionally it automatically returns
from functools import reduce

my_list = [1,2,3]

print(list(map(lambda item: item*2, my_list)))
print(my_list)

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc+item, my_list))

