
class Weapon:
    def strike(self, warrior, other):
        warrior.hp -= self.self_demage()
        other.hp -= self.demage()

    def demage(self):
        raise 'Not implemented'

    def self_demage(self):
        raise 'Not implemented'


class Sword(Weapon):
    def demage(self):
        return 10

    def self_demage(self):
        return 0

class Flamethrower(Weapon):
    def demage(self):
        return 50

    def self_demage(self):
        return 20

class Mace(Weapon):
    def demage(self):
        return 5

    def self_demage(self):
        return 2

class Enhanced(Weapon):
    def __init__(self, weapon):
        self.weapon = weapon

    def demage(self):
        return self.weapon.demage() * 2

    def self_demage(self):
        return self.weapon.self_demage() / 2

class Warrior:
    def __init__(self, weapon):
        self.hp = 100
        self.weapon = weapon

    def strike(self, opponent):
        self.weapon.strike(self, opponent)

    def __repr__(self):
        return 'Warrior hp:{}'.format(self.hp)

warrior = Warrior(Enhanced(Sword()))
monster = Warrior(Flamethrower())

warrior.strike(monster)
print(warrior)
print(monster)

monster.strike(warrior)
print(warrior)
print(monster)
