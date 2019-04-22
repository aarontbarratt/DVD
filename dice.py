import random


class Dice:

    def __init__(self, sides):
        self.sides = sides
        self.name = 'd' + str(sides)
        self.rolls = []
        self.roll_total = 0

    def roll(self, attempts=1, mode=0):

        # default mode 0, returns sum of all rolls
        if mode == 0:
            for _x in range(0, attempts):
                roll_value = random.randint(1, self.sides)
                self.roll_total = self.roll_total + roll_value
                self.rolls.append(roll_value)

            return self.roll_total

        # mode 1 returns the highest value
        if mode == 1:
            for _x in range(0, attempts):
                roll_value = random.randint(1, self.sides)
                self.rolls.append(roll_value)
            return max(self.rolls)

        # mode 2 returns the lowest value
        if mode == 2:
            for _x in range(0, attempts):
                roll_value = random.randint(1, self.sides)
                self.rolls.append(roll_value)
            return min(self.rolls)
