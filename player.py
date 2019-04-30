from dice import Dice
from dice import Modes
from inventory import Inventory


class Player:

    def __init__(self, name):
        # player name
        self.name = name

        # stats
        self.life = 1
        self.strength = 1
        self.dex = 1

        # roll stats
        self.roll_stats()

        # create bag
        self.bag = Inventory()

        # prompt used for player commands
        self.prompt = ''

        # current pos on map
        self.pos_x = 0
        self.pox_y = 0

        # player dice
        self.d3 = Dice(3)
        self.d6 = Dice(6)
        self.d12 = Dice(12)
        self.d20 = Dice(20)

    def roll_stats(self):
        # roll twice, use highest roll as stat
        #   uses players dice to roll
        self.life = self.d20.roll(2, Modes.highest)
        self.strength = self.d12.roll(2, Modes.highest)
        self.dex = self.d12.roll(2, Modes.highest)

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

    def who_am_i(self):
        print('My name is ' + self.name.title() + ', I think...')
