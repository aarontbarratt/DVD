from enum import Enum

from player import Player
from world import Map


class GameState(Enum):
    on = 1
    off = 0


class PlayerState(Enum):
    start = 0
    spawned = 1


class Command(Enum):
    look = 0
    walk = 1
    who_am_i = 2
    help = 1000
    exit = 1001


def player_command(prompt):
    prompt = prompt.replace(' ', '_')

    def print_commands(command_name, string):
        print(command_name.name.title() + ' > ' + string)

    if prompt == Command.look.name:
        player.look()

    elif prompt == Command.who_am_i.name:
        player.who_am_i()

    elif prompt == Command.exit.name:
        print('Goodbye! Thank you for playing.')
        global game_state
        game_state = GameState.off

    elif prompt == Command.help.name:
        for command in Command:
            if command == Command.look:
                print_commands(command, 'Look around the room to observe your surroundings.')

            elif command == Command.help:
                print_commands(command, 'Lists all commands')

            else:
                print_commands(command, 'ERROR: NO HELP DESCRIPTION')
    else:
        print(player.name + ' does not know what ' + '"' + str(prompt) + '"' + ' means')


def main_loop():
    while game_state == GameState.on:
        if player_state == PlayerState.start:
            print('you\'ve broken something')

        if player_state == player_state.spawned:
            player_command(input())
    else:
        print('mainloop broken')


# set the game state to on so that the main loop will continue to run
game_state = GameState.on

# first text the player sees
print('You wake up in a room that looks your grandma\'s mayo jar, and smells like grandma...\nYou scratch your head '
      'and attempt to remember your name.\nYour name is:', end=' ')

# get player name and create player class with it
player_name = input()
player_name_note = " ".join(player_name.upper().replace(' ', ''))
house = Map(player_name + ' house')
player = Player(player_name.lower().strip())
player.set_location(house.center, house.center)

# set player status to spawned
player_state = PlayerState.spawned

print('You check your bag and write down your name on a piece of paper. '
      '' + player_name_note + '.')

player.bag.add_item(name='Note', description='A note with the players name written on it', value=player_name_note)

print()

print("You check your map: ")
house.check_map()
house.check_connected(player.pos_x, player.pos_y)
house.check_room(player.pos_x, player.pos_y)

main_loop()
