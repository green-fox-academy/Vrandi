from random import randint

class Character:
    def __init__(self, name = None):
        self.name = name
        self.health = 0
        self.dexterity = 0
        self.max_health = 0

    def reenter_name(self):
        self.name = input('Add character name: ')

    def roll_stats(self):
        self.dexterity = self.roll_dice() + 6
        self.health = self.roll_dice() + self.roll_dice() + 12
        self.max_health = self.health

    def roll_dice(self):
        return randint(1, 6)

    def strike(self, other):
        myne = self.dexterity + self.roll_dice() + self.roll_dice()
        opponent = other.dexterity + self.roll_dice() + self.roll_dice()
        return myne, opponent

class Player(Character):
    def __init__(self):
        super().__init__()
        self.luck = 0
        self.inventory = ['Leather armor', 'Sword', 'potion']
        self.max_luck = 0

    def roll_stats(self):
        super().roll_stats()
        self.luck = self.roll_dice() + 6
        self.max_luck = self.luck

    def add_potion_to_inventory(self, potion):
        self.inventory = [potion if 'potion' in x.lower() else x for x in self.inventory]

    def __repr__(self):
        return '\ncharacter name: {}\ndexterity: {}\nhealth: {}\nmax-health: {}\nluck: {}\nmax-luck: {}\n'.format(self.name, self.dexterity, self.health, self.max_health, self.luck, self.max_luck)

    def display_character(self):
        print(self)
        print('Inventory: \n{}'.format('\n'.join([x for x in self.inventory])))

class Monster(Character):
    def reenter_name(self):
        self.name = input('Add monster name: ')

    def display_monster(self):
        print('\nmonsters name: {}\nmax-health: {}\nhealth: {}\ndexterity: {}\n'.format(self.name, self.health, self.max_health, self.dexterity))
