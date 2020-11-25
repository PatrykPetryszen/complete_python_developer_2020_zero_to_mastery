# Iterable it is an object or a collection that can be iterated over.
# Iterable can be list, dictionary, tuple, set, string

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
for item in user.items(): # .items() gives us key value pairs, .keys() or .values()
    print(item)

for key, value in user.items():
    print(key, value)