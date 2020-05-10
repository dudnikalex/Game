from Unit import *
from Warrior import *
from Archer import *
from Mage import *

import random

class Generator:

    def gen_war():
        return Warrior(random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100))

    def gen_mage():
        return Mage(random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100))
    
    def gen_arch():
        return Archer(random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100), random.randint(5, 100))
    