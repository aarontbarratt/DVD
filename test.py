# player command interp

# get player value
# split string on spaces


class CommandHandler:
    def __init__(self, player_input):
        # variables
        self.command = player_input.split()
        self.result = None

        if len(self.command) == 2:
            self.foo(self.command[0], self.command[1])

    def foo(self, command, arg):

        if command == 'walk':
            if arg == 'north':
                print('you walk north')
            elif arg == 'east':
                print('you walk east')
            elif arg == 'south':
                print('you walk south')
            elif arg == 'west':
                print('you walk west')
            else:
                print('unknown direction')
        else:
            print('unknown command')


ca = CommandHandler

while True:
    ca(input())
