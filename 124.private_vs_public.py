class PlayerCharacter(): #We don't need to use () if we are not inheriting
    def __init__(self, name, age):
        self._name = name # if we see _ it's a convention to say that this variable is private
        self._age = age # So it also means PLEASE DON'T TOUCH

    # def run(self):
    #     print('run')

    def speak(self):
        print(f'my name is {self._name}, and I am {self._age} years old')

player1 = PlayerCharacter('patryk', 26)
player1.name = '!!!'
player1.speak = 'BOOOO'

print(player1.speak)