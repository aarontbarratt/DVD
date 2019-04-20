from dice import Dice


def main():
    six_dye = Dice(1, 6)
    # six_dye.roll_additive(5)
    print(six_dye.roll_multiplicative(5))

main()
