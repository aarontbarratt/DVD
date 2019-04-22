from player import Player
from enum import Enum


aaron = Player('aaron')
aaron.roll_stats()
print(aaron.get_stats())
print(aaron.bag.slots[1].name)