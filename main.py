from dice import Dice


def main():
    six_dice = Dice(1, 6)
    thirteen_dice = Dice(1, 13)

    six_dice_roll = six_dice.roll_additive(2)
    thirteen_dice_roll = thirteen_dice.roll_additive(1)
    both_rolls = six_dice_roll + thirteen_dice_roll
    print(six_dice_roll, thirteen_dice_roll, both_rolls)


main()
