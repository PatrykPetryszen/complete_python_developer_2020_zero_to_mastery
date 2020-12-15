# This is Parent Class because the rest are inheriting from it
class User(object): # we don't need object in paranthesis but we did to show that Class User accepts objects
    def __init__(self, name, power, email):
        self.email = email
    
    def sign_in(self):
        print('logged in')

class Wizard(User): #Subclass, Children class or derived class as this is derived from User class
    def __init__(self, name, power, email):
        User.__init__(self, name, power, email) # Instead of this line we could use the next one with super
        #super().__init__(email) 
        # self.name = name
        # self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')


# isinstance(instance, Class) Method that tells you True/False

print(wizard1.email)

#introspection - ability to determine the type of the object at runtime (when the code is running)
#everything in Python is an object so we can introspect 
print(dir(wizard1))