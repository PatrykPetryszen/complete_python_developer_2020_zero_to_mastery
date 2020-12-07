#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# 1 Instantiate the Cat object with 3 cats

Filemon = Cat('Filemon', 2, 'male')
Garfield = Cat('Garfield', 3, 'male')
Nijok = Cat('Nijok', 5, 'female')

# 2 Create a function that finds the oldest cat

def get_oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {get_oldest_cat(Filemon.age, Garfield.age, Nijok.age)} years old.")