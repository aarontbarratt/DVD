from dice import Dice


def main():
    dice = Dice(1, 6)

    while True:
        print(dice.roll())


main()
