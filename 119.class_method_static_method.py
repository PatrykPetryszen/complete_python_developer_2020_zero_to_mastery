#OOP
class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name # attributes
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod # We can use classmethod without instantiating the class
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1+num2)

    @staticmethod
    def adding_thing2(num1, num2): # We don't have cls here
        return num1 + num2

# player1 = PlayerCharacter('Tom', 20)

player3 = PlayerCharacter.adding_things(2,3) # We can use this method using Class directly
# We don't often use classmethods
print(player3)
