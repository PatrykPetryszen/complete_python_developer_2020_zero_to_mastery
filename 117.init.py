#OOP
#To instantiate is to create an instance of an object
class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name='anonymous', age=0):
      if (age > 18):
        self.name = name # attributes
        self.age = age # self. refers to the class PlayerCharacter

    def run(self):
        print('run')    ## this function is just for demonstration can be deleted
        return 'done'

player1 = PlayerCharacter('Patryk', 26)
player2 = PlayerCharacter('Asia', 24)
player2.attack = 50

print(player1)
print(player2.name)
print(player2.age)
print(player2.attack)
print(player2.membership)