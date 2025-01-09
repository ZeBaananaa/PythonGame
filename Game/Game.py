import random
from enum import Enum
from os import system, name

from Player import *
from Collectible import *


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class GameState(Enum):
    LOST = 0,
    MAINMENU = 1,
    NAME_SELECTION = 2,
    PLAYING = 3


class Game:
    Ongoing = True
    State = GameState.MAINMENU

    def __init__(self):
        while self.Ongoing:
            # Game Lost Logic
            if self.State == GameState.LOST:
                clear()
                player_input = input("""
                            TOO BAD, YOU DIED!

                            If you would like to play again, type 'retry', otherwise type 'quit'.
                            """)

                if player_input == 'retry'.casefold():
                    self.State = GameState.NAME_SELECTION
                elif player_input == 'quit'.casefold() or player_input == 'exit'.casefold():
                    self.Ongoing = False
                else:
                    clear()
                    print('Invalid input. Try again!')

            # Main Menu
            if self.State == GameState.MAINMENU:
                clear()
                player_input = input("""
                            Available Commands:
                            Play - Start the game
                            Quit - Quit the game

                            Please enter your command : """).casefold()

                if player_input == "exit".casefold() or player_input == "quit".casefold():
                    self.Ongoing = False
                elif player_input == "start".casefold() or player_input == "play".casefold():
                    self.State = GameState.NAME_SELECTION
                else:
                    clear()
                    print('Invalid input. Try again!')

            # Name Selection
            if self.State == GameState.NAME_SELECTION:
                clear()
                player_input = input("Please enter your name : ")
                player = Player(player_input)

                print("Welcome to your new adventure, " + player.name + "!")
                print("Your Statistics : ")
                print("  - Health : " + str(player.health))
                print("  - Shield : " + str(player.shield))
                print("  - Base Damage : " + str(player.damage) + " | Damage Multiplier : " + str(
                    player.damage_multiplier) + " | Total Damage : " + str(
                    round(player.damage * player.damage_multiplier, 2)))
                print("  - Coins : " + str(player.coins))
                print("\n")
                print("You are an adventurer in a fantasy world. You decide to go on a short trip for fun.")
                self.State == GameState.PLAYING
                exploration_scenario(player)


def exploration_scenario(player: Player):
    clear()
    print("\nYou come across an ancient, overgrown ruin in the forest. What do you do?")
    print("1. Enter cautiously and search for treasure.")
    print("2. Study the inscriptions on the walls for clues about the ruin's origin.")
    print("3. Set a trap outside in case something dangerous emerges.")
    print("4. Leave the area, deciding it’s too risky.")

    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        print("You carefully enter and discover a chest filled with gold coins!")

        new_coins = random.randint(4, 15)
        print("Coins : " + str(player.coins) + " + " + str(new_coins))
        player.coins += new_coins

    elif choice == "2":
        print(
            "Studying ancient ruins is exhausting. You fall asleep, and when you wakeup, bandits have stolen all your coins.")

        player.coins = 0
        print("Coins : " + str(player.coins))

    elif choice == "3":
        print("You set up a trap and catch a sneaky bandit trying to ambush you.")
        bandit_fight(player)

    elif choice == "4":
        print("You decide to prioritize safety and leave the ruin behind.")

    else:
        print("Invalid choice. The moment passes uneventfully.")


def bandit_fight(player: Player):
    clear()
    print("\nThe bandit decides to try to fight against you, what do you do?")
    print("1. Fight back, let's see who's the chad here!")
    print("2. Run for your life (skill issue)")
    print("3. Try to negotiate with the bandit so no one gets hurt (Looks like someone is scared...)")

    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        print("You decide to be brave and try to fight the bandit")

        if player.final_damages >= 13:
            print(
                "Looks like you took the right choice, you're way stronger than the bandit, bro should've trained more!")

            potion = HealingPotion("Small Healing Potion", 10)

            print("You found a Small Healing Potion on his corpse! You decide to use it now.")
            potion.use(player)
            print("Health : " + str(player.health))

        elif player.final_damages < 15:
            print("You pissed off the bandit, whom decides to take your life as a revenge.")
            player.alive = False

    elif choice == "2":
        print(
            "Studying ancient ruins is exhausting. You fall asleep, and when you wakeup, bandits have stolen all your coins.")

        player.coins = 0
        print("Coins : " + str(player.coins))

    elif choice == "3":
        print("The bandit accepts to leave you alone, although it did cost you half your coins...")

        new_coins = player.coins * 0.5
        print("Coins : " + str(player.coins) + " - " + str(new_coins))
        player.coins = new_coins


game = Game()
