class Item:

    def __init__(self, name, description='an item', quantity=1, value=None):
        self.name = str(name).lower().strip()
        self.quantity = quantity
        self.description = description
        self.value = value


# not used, but demonstrates how you can create a class of another class type
class Weapon(Item):

    def __init__(self, damage):
        super().__init__('sword', 'sharp pointy thing')
        self.damage = damage
        self.strength = 10
        self.dex = 10
