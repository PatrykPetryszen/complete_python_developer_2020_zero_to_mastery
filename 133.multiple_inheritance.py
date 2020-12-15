class User(object):
    def __init__(self, email):
        self.email = email
        print('init complete')

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        self.name = name
        self.power = power
        super().__init__(email)

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

wizard1 = Wizard('Boogie', 50, 'thorin@op.pl')
print(wizard1.email)