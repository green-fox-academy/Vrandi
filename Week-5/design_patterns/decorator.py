'''Sword a csomag, a tobbi class mint a magical, enhanced a csomagolopapir'''

class Warrior:
    def __init__(self, weapon):
        self.hp = 100
        self.weapon = weapon

    def strike(self, other):
        demage = self.weapon.demage()
        other.hp -= demage

class Knife:
    def demage(self):
        return 3

class Sword:
    def demage(self):
        return 10

class Rusty:
    def __init__(self, weapon):
        self.weapon = weapon

    def demage(self):
        return self.weapon.demage() - 5

class Enhanced:
    def __init__(self, weapon):
        self.weapon = weapon

    def demage(self):
        return self.weapon.demage() + 5

class Magical:
    def __init__(self, weapon):
        self.weapon = weapon

    def demage(self):
        return self.weapon.demage()*2


warrior = Warrior(Magical(Enhanced(Sword())))
opponent = Warrior(Sword())

print(opponent.hp)
warrior.strike(opponent)
print(opponent.hp)
