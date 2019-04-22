from enum import Enum
from random import randint


class Modes(Enum):
    sum = 0
    highest = 1
    lowest = 2


class Dice:

    def __init__(self, sides):
        self.sides = sides
        self.name = 'd' + str(sides)
        self.rolls = []
        self.roll_total = 0

    def roll(self, attempts=1, mode=Modes.sum):

        # default mode 0, returns sum of all rolls
        if mode == Modes.sum:
            for _x in range(0, attempts):
                roll_value = randint(1, self.sides)
                self.roll_total = self.roll_total + roll_value
                self.rolls.append(roll_value)

            return self.roll_total

        # mode 1 returns the highest value
        if mode == Modes.highest:
            for _x in range(0, attempts):
                roll_value = randint(1, self.sides)
                self.rolls.append(roll_value)
            return max(self.rolls)

        # mode 2 returns the lowest value
        if mode == Modes.lowest:
            for _x in range(0, attempts):
                roll_value = randint(1, self.sides)
                self.rolls.append(roll_value)
            return min(self.rolls)
