user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 23
}

print(user['age']) # Alternatively we can use .get method

print(user.get('age'))

print(user.get('gender', 'There is no gender specified'))