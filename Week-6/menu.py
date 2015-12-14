
class Menu:
    def __init__(self, choices):
        self.choices = choices

    def __repr__(self):
        return '\n'.join([x.option + ' ' + x.text for x in self.choices])

    def invoke(self, choice):
        for item in self.choices:
            if choice == item.option:
                return item.function()

class MenuItem:
    def __init__(self, option, text, function):
        self.option = option
        self.text = text
        self.function = function
