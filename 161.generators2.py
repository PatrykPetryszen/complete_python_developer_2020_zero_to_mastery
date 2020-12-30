# list is iterable. Iterable is any object in Python that we are able to loop through
# generator is a subset of a list

# range is generator

def generator_function(num):
    for i in range(num):
        yield i*2 #Pass the function and yield i 

g = generator_function(100)
next(g)
next(g)
print(next(g))

# Compare with the commented

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(100)
# print(my_list)