from Hero import *
from Archer import *
from Warrior import *
from Mage import *
from Generator import *

import random

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