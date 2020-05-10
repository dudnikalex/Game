from Unit import *

class Archer(Unit):

    def __init__(self, hp, dm, ms, en, ag):
        Unit.__init__(self, hp, dm, ms, en)
        self.agility = ag

    def to_string(self):
        return "Archer with agility:" + str(self.agility) + " " + Unit.to_string(self)
