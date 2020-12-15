wizard = {
    'name': 'Merlin',
    'power': 50
}

# The idea is to keep data and functions separately

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))