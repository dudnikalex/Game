from Unit import *

class Warrior(Unit):

    def __init__(self, hp, dm, ms, en, st):
        Unit.__init__(self, hp, dm, ms, en)
        self.strength = st

    def to_string(self):
        return "Warrior with strenght:" + str(self.strength) + " " + Unit.to_string(self)

