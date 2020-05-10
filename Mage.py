from Unit import *

class Mage(Unit):

    def __init__(self, hp, dm, ms, en, intel):
        Unit.__init__(self, hp, dm, ms, en)
        self.intellect = intel

    def to_string(self):
        return "Mage with intellect:" + str(self.intellect) + " " + Unit.to_string(self)
