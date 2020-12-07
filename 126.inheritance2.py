# This is Parent Class because the rest are inheriting from it
class User(object): # we don't need object in paranthesis but we did to show that Class User accepts objects
    def sign_in(self):
        print('logged in')

class Wizard(User): #Subclass, Children class or derived class as this is derived from Usuer class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Merlin', 60)

# isinstance(instance, Class) Method that tells you True/False

print(isinstance(archer1, Wizard)) 
print(isinstance(archer1, User))

print(isinstance(wizard1, object))