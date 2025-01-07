from Player import Player

class Game:
    Ongoing = True

    def __init__(self):
        player = Player("Name", 100, 2)

        while Game.Ongoing:
            player_input = input("Enter a command:")

            if player_input == "exit":
                game.Ongoing = False

game = Game()