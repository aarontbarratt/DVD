from item import Item


class Inventory:

    def __init__(self):
        self.slots = []

    def add_item(self, name, description, value=None):
        self.slots.append(Item(str(name).lower(), str(description).lower(), 1, value))

    def get_items(self):
        for item in self.slots:
            print(str(item.quantity) + 'x : ' + item.name.title() + ', ' + item.description)
