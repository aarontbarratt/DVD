from enum import Enum
from player import Player


class GameState(Enum):
    on = 1
    off = 0


class PlayerState(Enum):
    start = 0
    spawned = 1


class Command(Enum):
    look = 0
    walk = 1
    exit = 999


def inputs(prompt):
    if prompt == Command.look.name:
        player.look()
    elif prompt == Command.exit.name:
        print('Goodbye! Thank you for playing.')
        exit()
    else:
        print(player.name + ' does not know what ' + '"' + str(prompt) + '"' + ' means')


def main_loop():
    while game_state == GameState.on:
        if player_state == PlayerState.start:
            print('you\'ve broken something')
        if player_state == player_state.spawned:
            player_input = input()
            inputs(player_input)


# set the game state to on so that the main loop will continue to run
game_state = GameState.on

# first text the player sees
print('You wake up in a room that looks your grandma\'s mayo jar, and smells like grandma... \n...\n...\n...\nYou'
      ' scratch your head and attempt to remember your name. Your name is:', end='')
# get player name and create player class with it
player_name = input()
player = Player(player_name.lower())

# set player status to spawned
player_state = PlayerState.spawned

main_loop()
