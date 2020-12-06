#OOP
class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
      if (PlayerCharacter.membership):
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