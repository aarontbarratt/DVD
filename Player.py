from dice import Dice
from dice import Modes
from inventory import Inventory

d6 = Dice(6)
d12 = Dice(12)
d20 = Dice(20)


class Player:

    def __init__(self, name):
        self.name = name
        self.life = 1
        self.strength = 1
        self.dex = 1
        self.bag = Inventory()
        self.prompt = ''

    def roll_stats(self):
        # roll twice, use highest roll as stat
        self.life = d20.roll(2, Modes.highest)
        self.strength = d12.roll(2, Modes.highest)
        self.dex = d12.roll(2, Modes.highest)

        # return results in list
        return self.life, self.strength, self.dex

    def get_stats(self):
        # returns stats in a list format
        return self.life, self.strength, self.dex

    def set_stats(self, life, strength, dex):
        # set stats with hard coded values
        self.life = life
        self.strength = strength
        self.dex = dex

        return self.life, self.strength, self.dex

    def look(self):
        print(self.name + ' looks around the room')
