
class Iterator:
    def __init__(self, list):
        self.list = list
        self.i = 0

    def next(self):
        self.i += 1
        return len(self.list) >= self.i

    def current(self):
        return self.list[self.i-1]*self.list[self.i-1]

l = [1,2,3,4]
iter = Iterator(l)
while iter.next():
    print(iter.current())
