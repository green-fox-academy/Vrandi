from character import Character

class Monster(Character):
    def strike(self, other):
        self.hp += 2
        super().strike(other)
