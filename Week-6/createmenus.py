from menu import *
import user

def create_quit_submenu():
    items = [
        MenuItem('1', 'Save and Quit', True),
        MenuItem('2', 'Quit', exit),
        MenuItem('0', 'Resume', True)
    ]
    return Menu(items)

def create_new_game_menu():
    userdude = user.User()
    items = [
        MenuItem('1', 'Reenter name', userdude.rename),
        MenuItem('2', 'Continue', True),
        MenuItem('3', 'Save', True),
        MenuItem('0', 'Quit', create_quit_submenu)
    ]
    print(userdude.name)
    return Menu(items)

def create_main_menu_list():
    items = [
        MenuItem('1', 'New Game', create_new_game_menu),
        MenuItem('2', 'Load Game', True),
        MenuItem('0', 'Exit', exit)
    ]
    return Menu(items)
