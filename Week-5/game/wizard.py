from character import Character

class Wizard(Character):
    def __init__(self, name, hp, damage, manna):
        super().__init__(name, hp, damage)
        self.manna = manna

    def strike(self, other):
        if self.manna > 5:
            other.hp -= self.damage * 3
            self.manna -= 5
        elif self.manna < 5:
            other.hp -= int(self.damage/3)
