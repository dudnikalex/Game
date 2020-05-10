class Unit:

    def __init__(self, hp, dm, ms, en):
        self.health = hp
        self.damage = dm
        self.movespeed = ms
        self.energy = en

    def to_string(self):
        return "hp:" + str(self.health) + " damage:" + str(self.damage) + " speed:" + str(self.movespeed) + " energy:" + str(self.energy)
