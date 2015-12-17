class MenuItem:
    def __init__(self, option, name, function):
        self.option = option
        self.name = name
        self.function = function

class Menu:
    def __init__(self, items):
        self.items = items

    def __repr__(self):
        return '\n'+'\n'.join(['{} {}'.format(item.option, item.name) for item in self.items])+'\n'

    def choiceinput(self):
        while True:
            try:
                choice = input('Choose from the menu: ')
                if not choice.isdigit() or int(choice) > len(self.items)-1:
                    raise ValueError
            except ValueError:
                print('Wrong input!')
            else:
                return choice
                break

    def invoke(self):
        choice = self.choiceinput()
        for item in self.items:
            if item.option == choice:
                return item.function()
