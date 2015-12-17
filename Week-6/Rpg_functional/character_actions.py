from character import *

gamers = []
monsters = []
loser = []

def create_character():
    gamer = Player()
    gamer.reenter_name()
    print('\nYour name is: {}\n'.format(gamer.name))
    gamers.append(gamer)

def rename_character():
    gamers[-1].reenter_name()
    print('\nYour name is: {}\n'.format(gamers[-1].name))

def roll_stats():
    current_gamer = gamers[-1]
    current_gamer.roll_stats()
    print(current_gamer)

def add_potion(choice):
    potions = {'1': 'Potion of health', '2':'Potion of dexterity', '3':'Potion of luck'}
    current_gamer = gamers[-1]
    current_gamer.add_potion_to_inventory(potions[choice])
    print(current_gamer.inventory[-1])

def character_info():
    gamers[-1].display_character()

def test_fight():
    monster = Monster()
    monster.reenter_name()
    monster.roll_stats()
    monsters.append(monster)
    print('Test your sward in a test fight!')
    print(gamers[-1])
    monster.display_monster()

def strike():
    current_gamer = gamers[-1]
    monster = monsters[-1]
    gamerdex, monsterdex = current_gamer.strike(monster)
    if gamerdex > monsterdex:
        print('You hit the monster!')
        loser.append(monster)
    else:
        print('The monster hit you!')
        loser.append(current_gamer)

def substract_from_loser():
    loser[-1].health -= 2
