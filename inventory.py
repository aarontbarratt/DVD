class Inventory:

    def __init__(self, inventory_space=10):
        self.slots = []
        self.inventory_space = inventory_space

        for _x in range(0, self.inventory_space):
            self.slots.append(Slot(_x))


class Slot:

    def __init__(self, number):
        self.name = number
        self.item = None  # this will be used as the item object later
