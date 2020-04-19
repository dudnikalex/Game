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
    
names = ['Slaveslav', 'Rashid', 'Veniamin', 'Herr']

class Hero:
    types = ['Paladin', 'Archer', 'Mage']

    def __init__(self, name=None, type1=None):
        if name == None and type1 == None:
            self.__init__1()
            return 
        self.name = name
        self.type = type1

    def __init__1(self):
        global names
        ind2 = random.randint(0, 2)
        self.name = names[0]
        names.pop(0)
        self.type = self.types[ind2]

class Squad(Unit, Hero):

    def __init__(self, units=None, hero=None):
        if units == None and hero == None:
            self.__init__1()
            return
        self.hero = hero
        self.units = units
        self.money = 100
        self.score = 0

    def __init__1(self):
        self.hero = Hero()
        self.units = []

        num1 = random.randint(1, 5)
        num2 = random.randint(0, 5 - num1)
        num3 = random.randint(0, 5 - num1 - num2)

        for i in range(num1):
            self.units.append(Generator.gen_war())

        for i in range(num2):
            self.units.append(Generator.gen_mage())

        for i in range(num3):
            self.units.append(Generator.gen_arch())

        self.score = random.randint(5, 100)
        
    def to_string(self):
        return "Squad with " + self.hero.type + " " + self.hero.name + " and " + str(len(self.units)) + " units. It's score is " + str(self.score) + "."