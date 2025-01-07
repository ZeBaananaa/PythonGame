from enum import Enum

from Player import Player

class GameState(Enum):
    MAINMENU = 0,
    PLAYING = 1,
    LOST = 2,

class Game:
    Ongoing = True
    State = GameState.MAINMENU

    def __init__(self):
        while self.Ongoing:
            if self.State == GameState.MAINMENU:
                player_input = input("Available Commands: \nPlay - Start the game \nQuit - Quit the game \n\nPlease enter your command: ").casefold()

                if player_input == "exit".casefold() or player_input == "quit".casefold():
                    self.Ongoing = False
                if player_input == "start".casefold() or player_input == "play".casefold():
                    self.State = GameState.PLAYING

            if self.State == GameState.PLAYING:
                player_input = input("Please enter your name: ")
                player = Player(player_input, 100, 2)

                print("Your name is " + player.name)

game = Game()