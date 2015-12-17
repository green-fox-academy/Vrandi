from menu_class import *
from character import *

gamers = []
monsters = []

def new_game():
    gamer = Player()
    gamer.reenter_name()
    print('\nYour name is: {}\n'.format(gamer.name))
    gamers.append(gamer)
    main(new_game_menu)

def reenter_name():
    current_gamer = gamers[-1]
    current_gamer.reenter_name()
    print('\nYour name is: {}\n'.format(current_gamer.name))
    main(new_game_menu)

def roll_stats_continue():
    current_gamer = gamers[-1]
    current_gamer.roll_stats()
    print(current_gamer)
    main(roll_stats)

def continue_potion():
    main(choice_potion)

def choose_potion_of_health():
    current_gamer = gamers[-1]
    current_gamer.add_potion_to_inventory('Potion of health')
    print(current_gamer.inventory[-1])
    main(potion_choosed)

def choose_potion_of_luck():
    current_gamer = gamers[-1]
    current_gamer.add_potion_to_inventory('Potion of luck')
    print(current_gamer.inventory[-1])
    main(potion_choosed)

def choose_potion_of_dexterity():
    current_gamer = gamers[-1]
    current_gamer.add_potion_to_inventory('Potion of dexterity')
    print(current_gamer.inventory[-1])
    main(potion_choosed)

def continue_begin():
    current_gamer = gamers[-1]
    current_gamer.display_character()
    main(begin)

def test_fight():
    monster = Monster()
    monster.reenter_name()
    monster.roll_stats()
    monsters.append(monster)
    current_gamer = gamers[-1]
    print('Test your sward in a test fight!')
    print(current_gamer)
    monster.display_monster()
    main(begin_fight)


def strike():
    current_gamer = gamers[-1]
    monster = monsters[-1]
    gamerdex, monsterdex = current_gamer.strike(monster)


main_menu = Menu([
    MenuItem('1', 'New game', new_game),
    MenuItem('2', 'Load game', True),
    MenuItem('0', 'Quit', exit)
])

new_game_menu = Menu([
    MenuItem('1', 'Reenter name', reenter_name),
    MenuItem('2', 'Continue', roll_stats_continue),
    MenuItem('3', 'Save', True),
    MenuItem('0', 'Quit', True)
])

quit_menu = Menu([
    MenuItem('1', 'Save and Quit', True),
    MenuItem('2', 'Resume', True),
    MenuItem('0', 'Quit', exit)
])

roll_stats = Menu([
    MenuItem('1', 'Reroll Stats', roll_stats_continue),
    MenuItem('2', 'Continue', continue_potion),
    MenuItem('3', 'Save', True),
    MenuItem('0', 'Quit', True)
])

choice_potion = Menu([
    MenuItem('0', 'Potion of health', choose_potion_of_health),
    MenuItem('1', 'Potion of dexterity', choose_potion_of_dexterity),
    MenuItem('2', 'Potion of luck', choose_potion_of_luck)
])

potion_choosed = Menu([
    MenuItem('1', 'Reselect Potion', continue_potion),
    MenuItem('2', 'Continue', continue_begin),
    MenuItem('0', 'Quit', True)
])

begin = Menu([
    MenuItem('1', 'Begin', test_fight),
    MenuItem('2', 'Save', True),
    MenuItem('0', 'Quit', True)
])

begin_fight = Menu([
    MenuItem('1', 'Strike', True),
    MenuItem('2', 'Retreat', continue_begin),
    MenuItem('0', 'Quit', True)
])

hit = Menu([
    MenuItem('1', 'Continue', True),
    MenuItem('2', 'Try your Luck', True),
    MenuItem('3', 'Retreat', True),
    MenuItem('0', 'Quit', True)
])

def main(actual_menu):
    print(actual_menu)
    actual_menu.invoke()

main(main_menu)
