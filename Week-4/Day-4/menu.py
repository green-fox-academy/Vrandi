import todo as t
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def print_menu():
    print(
        '*'*32,
        '\n*'+'\t'*3+'1: List current items'+'\t'*4+'*',
        '\n*'+'\t'*3+'2: Add new items'+'\t'*4+'*',
        '\n*'+'\t'*3+'3: Move item'+'\t'*5+'*',
        '\n*'+'\t'*3+'4: List Doing items'+'\t'*4+'*',
        '\n*'+'\t'*3+'5: List Done items'+'\t'*4+'*',
        '\n*'+'\t'*3+'6: Remove item'+'\t'*5+'*',
        '\n*'+'\t'*3+'7: Erase list'+'\t'*5+'*',
        '\n*'+'\t'*3+'X: Exit'+'\t'*2,
        '*'*32
        )

def main():
    cls()
    print('*'*23+' Welcome to your todo list! '+'*'*22+ '\n')
    todo = t.Todo()
    ch = ''
    while ch.lower() != 'x':
        print_menu()
        ch = input("\nChoose from the menu: ")
        cls()
        if ch == '1':
            todo.print_current()
        elif ch == '2':
            todo.add_item()
        elif ch == '3':
            move = input('Choose a path (current > doing (c) or doing > done (d)): ').lower()
            if move == 'c':
                todo.move_to_doing()
            elif move == 'd':
                todo.move_to_done()
            else:
                print('Sorry wrong input')
        elif ch == '4':
            todo.print_doing()
        elif ch == '5':
            todo.print_done()
        elif ch == '6':
            path = input('Choose a list: current (c), doing (d), done (n): ').lower()
            if path == 'c':
                todo.remove_item_current()
            elif path == 'd':
                todo.remove_item_doing()
            elif path == 'n':
                todo.remove_item_done()
            else:
                print('Sorry wrong input')
        elif ch == '7':
            path = input('Choose a list: current (c), doing (d), done (n): ').lower()
            if path == 'c':
                todo.erase_current()
            elif path == 'd':
                todo.erase_doing()
            elif path == 'n':
                todo.erase_done()
            else:
                print('Sorry wrong input')
        elif ch.lower() == 'x':
            print('Have a nice day!')
        else:
            print("I don't understand try again!")

main()
