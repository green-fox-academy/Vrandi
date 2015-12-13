class Ship:
    def __init__(self, status=False):
        self.status = status

    def statuschanger(self):
        self.status = True

class AircraftCarrier(Ship):
    fieldnum = 5
    def __init__(self, position):
        super().__init__()
        self.position = position

class Battleship(Ship):
    fieldnum = 4
    def __init__(self, position):
        super().__init__()
        self.position = position

class Submarine(Ship):
    fieldnum = 3
    def __init__(self, position):
        super().__init__()
        self.position = position

class Destroyer(Ship):
    fieldnum = 3
    def __init__(self, position):
        super().__init__()
        self.position = position

class PatrolBoat(Ship):
    fieldnum = 2
    def __init__(self, position):
        super().__init__()
        self.position = position
