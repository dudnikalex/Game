import random

names = ['Slaveslav', 'Rashid', 'Veniamin', 'Herr', "Hadsas", "Asdasd", "Sdasdsa"]

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
