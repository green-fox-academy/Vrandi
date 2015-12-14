from createmenus import *
from menu import *

def main():
    m = create_main_menu_list()
    new = m
    while True:
        try:
            print(new)
            choice = input('\nChoose from the menu: ')
            print('\n')
            if not choice.isdigit() or int(choice) > len(new.choices)-1:
                raise ValueError
        except ValueError:
            print('Wrong input')
            choice = input('\nChoose again from the menu: ')
        new = new.invoke(choice)

main()
