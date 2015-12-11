
class Warrior:
    def __init__(self):
        self.companions = []
        self.hp = 100
        self.potions = 0

    def join(self, companion):
        self.companions.append(companion)

    def strike(self, opponent):
        opponent.inflict_demage(10)

    def inflict_demage(self, demage):
        self.hp -= demage
        for companion in self.companions:
            companion.notify('demage', self)

    def heal(self, hp):
        self.hp += hp
        for companion in self.companions:
            companion.notify('healed', self)

    def back_on(self):
        print("I'm healed! Back on")

    def bitten_by_a_pet(self, demage):
        self.hp -= demage

class Pet:
    def notify(self, type, warrior):
        if type == 'demage':
            warrior.bitten_by_a_pet(3)

class Healer:
    def notify(self, type, warrior):
        if type == 'demage':
            warrior.heal(10)
        if type == 'healed':
            warrior.back_on()


rabbit = Warrior()
wolf = Warrior()
#doggy = Pet()
shaman = Healer()

rabbit.join(shaman)
#rabbit.join(doggy)
wolf.strike(rabbit)
print(rabbit.hp)
print(wolf.hp)
