# map, filter, zip and reduce

# map(action, [1,2,3])

def multiply_by2(li):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2) When using map we can get rid off this part 
    # return new_list
    return li*2



print(list(map(multiply_by2, [1,2,3]))) #We use list to convert the output
                                        # to the list because map returns object location