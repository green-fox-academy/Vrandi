class Game:
    def __init__(self):
        self.items = {}

    def register_action(self, option, function):
        self.items[option] = function

    def startgame(self, next):
        while True:
            next = self.items[next]()
            if next == 'exit':
                break
