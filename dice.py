import random


class Dice:
    def __init__(self, min_roll, max_roll):
        self.min_roll = min_roll
        self.max_roll = max_roll

    def roll(self):
        result = random.randint(self.min_roll, self.max_roll)
        return result
