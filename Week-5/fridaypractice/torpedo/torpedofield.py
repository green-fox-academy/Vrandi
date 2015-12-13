
class Field:
    def __init__(self, index, status=False):
        self.index = index
        self.status = status

    def statuschanger(self):
        self.status = True

class Shipfield(Field):
    pass
