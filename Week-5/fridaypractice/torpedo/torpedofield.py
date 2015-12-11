
field = [
    [1,1,0,1,0,0,1,1,1,1],
    [0,0,0,1,0,0,0,0,0,0],
    [1,0,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,1,0,0,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,1]
]

class Field:
    def __init__(self, xindex, yindex, status):
        self.xindex = xindex
        self.yindex = yindex
        self.status = status

    def statuschanger(self):
        self.status = True

class Shipfield(Field):
    def __init__(self, xindex, yindex, status):
        super.__init__()
