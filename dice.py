import random


class Dice:
    def __init__(self, min_roll, max_roll):
        self.min_roll = min_roll
        self.max_roll = max_roll
        self.number_of_rolls = 1
        self.result = 0
        self.total = 0

    def roll_additive(self, number_of_rolls):
        self.number_of_rolls = number_of_rolls

        for x in range(0, self.number_of_rolls):
            self.result = random.randint(self.min_roll, self.max_roll)
            self.total = self.total + self.result
        return self.total

    def roll_multiplicative(self, number_of_rolls):
        self.number_of_rolls = number_of_rolls

        for x in range(0, self.number_of_rolls):
            self.result = random.randint(self.min_roll, self.max_roll)
            if x == 0:
                self.total = self.result
            else:
                self.total = self.total * self.result

        return self.total
