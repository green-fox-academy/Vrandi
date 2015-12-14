
class User:
    def __init__(self):
        name = input('Add user name: ')
        self.name = name

    def rename(self):
        new = input('Add new user name: ')
        self.name = new
        return self.name
