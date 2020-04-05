import random


class Unit:

    def __init__(self, hp, dm, ms, en):
        self.health = hp
        self.damage = dm
        self.movespeed = ms
        self.energy = en

    def to_string(self):
        return "hp: " + str(self.health) + "; damage: " + str(self.damage) + "; movement speed: " + str(self.movespeed) + "; energy: " + str(self.energy)

    def get_damage(self, dhp):
        self.hp -= dhp


class Warrior(Unit):

    def __init__(self, hp, dm, ms, en, st):
        Unit.__init__(self, hp, dm, ms, en)
        self.strength = st

    def to_string(self):
        return "Warrior with strenght: " + str(self.strength) + "; " + Unit.to_string(self)


class Mage(Unit):

    def __init__(self, hp, dm, ms, en, intel):
        Unit.__init__(self, hp, dm, ms, en)
        self.intellect = intel

    def to_string(self):
        return "Mage with intellect: " + str(self.intellect) + "; " + Unit.to_string(self)


class Archer(Unit):

    def __init__(self, hp, dm, ms, en, ag):
        Unit.__init__(self, hp, dm, ms, en)
        self.agility = ag

    def to_string(self):
        return "Archer with agility: " + str(self.agility) + "; " + Unit.to_string(self)

class Generator:

    def gen_war():
        return Warrior(random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100))

    def gen_mage():
        return Mage(random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100))
    
    def gen_arch():
        return Archer(random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100))