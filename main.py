from enum import Enum


class GameState(Enum):
    on = 1
    off = 0


class StoryState(Enum):
    first_spawn = 0
    spawned = 0


class Commands(Enum):
    look = 0
    walk = 1


class GameLogic:

    def __init__(self, player_command):
        self.input = str(player_command).lower

    def route_action(self):
        if self.input == Commands.look:
            print('player looks around')
        if self.input == Commands.walk:
            print('player walks around')


def main():
    game_state = GameState.on
    story_state = StoryState.first_spawn

    while game_state == GameState.on:
        if story_state == StoryState.first_spawn:
            print('You spawn, dazed and confused')
        player_input = input()
        GameLogic(player_input)


main()
