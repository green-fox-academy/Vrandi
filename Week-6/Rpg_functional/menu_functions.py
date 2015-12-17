from menu_class import *
from character_actions import *

def print_main_menu():
    l = [('1', 'New game'), ('2', 'Load game'), ('0', 'Quit')]
    print('\n'+'\n'.join([x[0] + ' ' + x[1] for x in l])+'\n')
    menu = {x[0]:x[1] for x in l}
    choosen_menu_id = input('Choose from the menu: ')
    return menu[choosen_menu_id]

def new_game_menu():
    l = [
        ('1', {'title': 'Reenter name', 'id':'new_reenter'}),
        ('2', {'title': 'Continue', 'id':'stats'}),
        ('3', {'title': 'Save', 'id' : 'new'}),
        ('0', {'title': 'Quit', 'id': 'exit' })
    ]
    print('\n'+'\n'.join([x[0] + ' ' + x[1]['title'] for x in l])+'\n')
    menu = {x[0]: x[1] for x in l}
    choosen_menu_id = input('Choose from the menu: ')
    return menu[choosen_menu_id]['id']

def print_new_game():
    create_character()
    return new_game_menu()

def reenter_name():
    rename_character()
    return new_game_menu()

def roll_stats_menu():
    roll_stats()
    l = [('1', {'title':'Reroll stats', 'id':'stats'}),
        ('2', {'title':'Continue', 'id':'statcontinue'}),
        ('3', {'title':'Save', 'id':'save'}),
        ('0', {'title':'Quit', 'id':'exit'})]
    print('\n'+'\n'.join([x[0] + ' ' + x[1]['title'] for x in l])+'\n')
    menu = {x[0]: x[1] for x in l}
    choosen_menu_id = input('Choose from the menu: ')
    return menu[choosen_menu_id]['id']

def potion_menu():
    l = [('1', {'title': 'Potion of health', 'id':'potion'}),
        ('2', {'title': 'Potion of dexterity', 'id':'potion'}),
        ('3', {'title': 'Potion of luck', 'id':'potion'}),]
    print('\n'+'\n'.join([x[0] + ' ' + x[1]['title'] for x in l])+'\n')
    menu = {x[0]: x[1] for x in l}
    choosen_menu_id = input('Choose from the menu: ')
    add_potion(choosen_menu_id)
    return menu[choosen_menu_id]['id']

def selected_potion():
    l = [('1', {'title': 'Reselect potion', 'id':'statcontinue'}),
        ('2', {'title': 'Continue', 'id':'begin'}),
        ('0', {'title': 'Quit', 'id':'exit'}),]
    print('\n'+'\n'.join([x[0] + ' ' + x[1]['title'] for x in l])+'\n')
    menu = {x[0]: x[1] for x in l}
    choosen_menu_id = input('Choose from the menu: ')
    return menu[choosen_menu_id]['id']

def begin():
    character_info()
    l = [('1', {'title': 'Begin', 'id':'begin_fight'}),
        ('2', {'title': 'Save', 'id':'save'}),
        ('0', {'title': 'Quit', 'id':'exit'}),]
    print('\n'+'\n'.join([x[0] + ' ' + x[1]['title'] for x in l])+'\n')
    menu = {x[0]: x[1] for x in l}
    choosen_menu_id = input('Choose from the menu: ')
    return menu[choosen_menu_id]['id']

def begin_fight():
    test_fight()
    l = [('1', {'title': 'Strike', 'id':'strike'}),
        ('2', {'title': 'Retreat', 'id':'ret'}),
        ('0', {'title': 'Quit', 'id':'exit'}),]
    print('\n'+'\n'.join([x[0] + ' ' + x[1]['title'] for x in l])+'\n')
    menu = {x[0]: x[1] for x in l}
    choosen_menu_id = input('Choose from the menu: ')
    return menu[choosen_menu_id]['id']

def begin_strike():
    strike()
    l = [('1', {'title': 'Continue', 'id':'afterstrike'}),
        ('2', {'title': 'Try your Luck', 'id':'luck'}),
        ('3', {'title': 'Retreat', 'id':'retreat'}),
        ('0', {'title': 'Quit', 'id':'exit'}),]
    print('\n'+'\n'.join([x[0] + ' ' + x[1]['title'] for x in l])+'\n')
    menu = {x[0]: x[1] for x in l}
    choosen_menu_id = input('Choose from the menu: ')
    return menu[choosen_menu_id]['id']

def after_strike():
    substract_from_loser()
    return begin_fight()

game = Game()
game.register_action('print_main_menu', print_main_menu)
game.register_action('New game', print_new_game)
game.register_action('new_reenter', reenter_name)
game.register_action('stats', roll_stats_menu)
game.register_action('statcontinue', potion_menu)
game.register_action('potion', selected_potion)
game.register_action('begin', begin)
game.register_action('begin_fight', begin_fight)
game.register_action('strike', begin_strike)
game.register_action('afterstrike', after_strike)
game.register_action('exit', exit)
game.startgame('print_main_menu')
