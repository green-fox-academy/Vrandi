from handlefile import *

createfile('todo.txt')
createfile('doing.txt')
createfile('done.txt')

class Todo:
    def __init__(self):
        self.currentitems = fileread('todo.txt')
        self.doing = fileread('doing.txt')
        self.done = fileread('done.txt')

    def add_item(self):
        new_item = input('Add new item to do list: ')
        while new_item != '':
            self.currentitems.append(new_item)
            writefile('todo.txt', self.currentitems)
            new_item = input('Add new item to do list: ')

    def remove_item(self, froml, file_name):
        for i, e in enumerate(froml):
            print('{}: {}'.format(i+1, e))
        ch = int(input('Choose which item you want to remove:'))-1
        froml.pop(ch)
        writefile(file_name, froml)

    def remove_item_current(self):
        print('Current Items in Todo List: \n\n')
        self.remove_item(self.currentitems, 'todo.txt')

    def remove_item_doing(self):
        print('Current Items in Doing List: \n\n')
        self.remove_item(self.doing, 'doing.txt')

    def remove_item_done(self):
        print('Current Items in Done List: \n\n')
        self.remove_item(self.done, 'done.txt')

    def erase_current(self):
        self.currentitems[:] = []
        writefile('todo.txt', self.currentitems)

    def erase_doing(self):
        self.doing[:] = []
        writefile('doing.txt', self.doing)

    def erase_done(self):
        self.done[:] = []
        writefile('done.txt', self.done)

    def move_to_doing(self):
        self.print_current()
        ch = int(input('Choose which item you are doing:'))-1
        doing = self.currentitems[ch]
        self.doing.append(doing)
        writefile('doing.txt', self.doing)
        self.currentitems.pop(ch)
        writefile('todo.txt', self.currentitems)

    def move_to_done(self):
        self.print_doing()
        ch = int(input('Choose the item you already done: '))-1
        done = self.doing[ch]
        self.done.append(done)
        writefile('done.txt', self.done)
        self.doing.pop(ch)
        writefile('doing.txt', self.doing)

    def print_current(self):
        st = '\nCurrent Items in Todo List: \n\n'
        for i, e in enumerate(self.currentitems):
            st +='{}: {}\n'.format(i+1, e)
        print(st)

    def print_doing(self):
        st = '\nYou are doing: \n\n'
        for i, e in enumerate(self.doing):
            st +='{}: {}\n'.format(i+1, e)
        print(st)

    def print_done(self):
        st = '\nDone items: \n\n'
        for i, e in enumerate(self.done):
            st +='{}: {}\n'.format(i+1, e)
        print(st)
