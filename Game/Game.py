import os
from time import sleep
from Player import *
from enum import Enum


def clear_console():
    # for windows
    if os.name == "nt":
        os.system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system("clear")


class GameState(Enum):
    LOST = 0
    MAINMENU = 1
    NAME_SELECTION = 2
    PLAYING = 3
    ENDING = 4


class GameCommands(Enum):
    QUIT_EXIT = ["quit", "exit"]
    START = "start"
    PLAY = "play"


def display_end_game_stats(player, win: bool):
    clear_console()

    if win:
        print("\nCongratulations! You managed to survive! Here are your final statistics:")
    else:
        print("\nGame Over! Here are your final statistics:")

    print(f"Name : {player.name}")
    print(f"Health : {player.health}")
    print(f"Shield : {player.shield}")
    print(f"Damage : {player.damage}")
    print(f"Damage Multiplier : {player.damage_multiplier}")
    print(f"Total Damage : {round(player.damage * player.damage_multiplier, 2)}")
    print(f"Coins : {player.coins}")
    sleep(8)


class Game:
    ongoing = True
    current_state = GameState.MAINMENU

    def __init__(self, player=None):
        while self.ongoing:
            if self.current_state is GameState.LOST:

                clear_console()
                player_input = input("""
                            TOO BAD, YOU DIED!

                            If you would like to play again, type 'retry', otherwise type 'quit'.
                            """)

                if player_input.casefold() == "retry":
                    self.current_state = GameState.NAME_SELECTION
                elif player_input.casefold() in GameCommands.QUIT_EXIT:
                    display_end_game_stats(player, False)

                    self.ongoing = False
                else:
                    clear_console()
                    print('Invalid input. Try again!')

            # Main Menu
            if self.current_state == GameState.MAINMENU:

                clear_console()
                player_input = input("""
                            Available Commands:
                            Play - Start the game
                            Quit - Quit the game

                            Please enter your command : """).casefold()

                if player_input.casefold() in GameCommands.QUIT_EXIT.value:
                    display_end_game_stats(Player("Guest"), False)

                    self.ongoing = False
                elif player_input.casefold() in [GameCommands.START.value, GameCommands.PLAY.value]:
                    self.current_state = GameState.NAME_SELECTION
                else:
                    clear_console()
                    print('Invalid input. Try again!')

            # Name Selection
            if self.current_state == GameState.NAME_SELECTION:
                clear_console()
                player_input = input("Please enter your name : ")
                player = Player(player_input)
                print(f"Welcome to your new adventure, {player.name}!")
                print("Your Statistics : ")
                print(f"  - Health : {player.health}")
                print(f"  - Base Damage : {player.damage} | Damage Multiplier: {player.damage_multiplier} | Total Damage: {round(player.damage * player.damage_multiplier, 2)}")
                print(f"  - Coins : {player.coins}")
                print("\n")
                print("You are an adventurer in a fantasy world. You decide to go on a short trip for fun.")
                sleep(7)
                self.current_state = GameState.PLAYING
                self.exploration_scenario(player)


    @staticmethod
    def exploration_scenario(player: Player):

        clear_console()
        choices = [
            "Enter cautiously and search for treasure.",
            "Study the inscriptions on the walls for clues about the ruin's origin.",
            "Set a trap outside in case something dangerous emerges.",
            "Leave the area, deciding it’s too risky."
        ]
        print("\nYou come across an ancient, overgrown ruin in the forest. What do you do?")
        for i, player_choice in enumerate(choices, start=1):
            print(f"{i}. {player_choice}")

        player_choice = input("Enter your choice (1-4): ")
        match player_choice:
            case "1":
                print("You carefully enter and discover a chest filled with gold coins!")
                player.coins += random.randint(4, 15)
                print("Coins : " + str(player.coins))
                sleep(4)
                Game.fork_in_the_road(player)

            case "2":
                print("Studying ancient ruins is exhausting. You fall asleep, and when you wakeup, bandits have stolen all your coins.")
                player.coins = 0
                print("Coins : " + str(player.coins))
                sleep(4)
                Game.fork_in_the_road(player)

            case "3":
                print("You set up a trap and catch a sneaky bandit trying to ambush you.")
                sleep(2)
                Game.bandit_fight_scenario(player)

            case "4":
                print("You decide to prioritize safety and leave the ruin behind.")
                sleep(2)
                Game.fork_in_the_road(player)

            case _:
                print("Invalid choice. Please choose a number between 1-4!")


    @staticmethod
    def bandit_fight_scenario(player: Player):

        clear_console()
        print("\nThe bandit decides to try to fight against you, what do you do?")
        print("1. Fight back, let's see who's the chad here!")
        print("2. Run for your life (skill issue)")
        print("3. Try to negotiate with the bandit so no one gets hurt (Looks like someone is scared...)")

        choice = input("Enter your choice (1-3): ")
        match choice:
            case "1":
                print("You decide to be brave and try to fight the bandit")

                if player.final_damages >= 13:
                    print("Looks like you took the right choice, you're way stronger than the bandit, bro should've trained more!")
                    potion = HealingPotion("Small Healing Potion", 10)

                    print("You found a Small Healing Potion on his corpse! You decide to use it now.")
                    potion.use(player)
                    print(f"Health: {player.health}")
                    sleep(7)
                    Game.fork_in_the_road(player)

                elif player.final_damages < 13:
                    print("You pissed off the bandit, whom decides to take your life as a revenge.")
                    sleep(4)
                    display_end_game_stats(player, False)

            case "2":
                print("You decide to run for your life and manage to escape the bandit with no injuries.")
                sleep(3)
                Game.fork_in_the_road(player)

            case "3":
                print("You negotiate with the bandit and they agree to leave you alone, although it did cost you half your coins...")

                new_coins = player.coins * 0.5
                print(f"Coins : {player.coins} + {new_coins}")
                player.coins = new_coins
                sleep(5)
                Game.fork_in_the_road(player)

            case _:
                print("Invalid choice. Please choose a valid option (1-3).")


    @staticmethod
    def fork_in_the_road(player: Player):

        clear_console()
        print("\nDuring your journey, you arrive at a fork in the road. What do you do?")
        print("1. Take the well-trodden path that seems safe.")
        print("2. Take the overgrown path that looks mysterious.")
        print("3. Camp for the night and decide in the morning.")

        choice = input("Enter your choice (1-3): ")
        match choice:
            case "1":
                print("You safely reach a friendly village and find an item shop.")
                item = HealingPotion("Medium Healing Potion", 20)
                print("You buy a Medium Healing Potion for 5 coins and use it!")
                player.coins -= 5
                item.use(player)
                print(f"Health: {player.health}, Coins: {player.coins}")
                sleep(8)
                Game.mysterious_merchant(player)

            case "2":
                print("You encounter a pack of wild animals but manage to scare them off.")
                damage = random.randint(10, 40)
                print(f"The wild animals hurt you! Health: {player.health} - {damage}")
                player.health -= damage

                if player.health <= 0:
                    print("Unfortunately, your injuries were fatal.")
                    sleep(5)
                    player.alive = False
                    display_end_game_stats(player, False)
                else:
                    sleep(5)
                    Game.mysterious_merchant(player)

            case "3":
                print("You wake up in the morning feeling refreshed. Nothing of interest happens.")
                print("You continue your journey.")
                sleep(5)
                Game.mysterious_merchant(player)

            case _:
                print("Invalid choice. A few hours pass without action.")


    @staticmethod
    def mysterious_merchant(player: Player):
        clear_console()
        print("\nA mysterious merchant appears on your path with rare wares. What do you do?")
        print("1. Buy a mysterious scroll for 10 coins.")
        print("2. Attack the merchant and take his items.")
        print("3. Ignore the merchant and continue on your way.")

        choice = input("Enter your choice (1-3): ")
        match choice:
            case "1":
                if player.coins >= 10:
                    print("You buy the mysterious scroll. It grants you +5 damage forever!")
                    player.coins -= 10
                    player.damage += 5
                    print(f"Damage: {player.damage}, Coins: {player.coins}")
                    sleep(5)
                else:
                    print("You don't have enough coins to buy the scroll. The merchant leaves!")
                    sleep(3)
                Game.abandoned_campfire(player)

            case "2":
                print("The merchant reveals himself to be a powerful wizard and casts a spell on you!")
                health_loss = random.randint(10, 20)
                print(f"You lose {health_loss} health and barely escape.")
                player.health -= health_loss
                sleep(5)
                Game.abandoned_campfire(player)

            case "3":
                print("You leave the merchant behind and continue traveling. He mutters something under his breath.")
                sleep(3)
                Game.abandoned_campfire(player)

            case _:
                print("Invalid choice. The merchant vanishes into thin air.")


    @staticmethod
    def abandoned_campfire(player: Player):
        clear_console()
        print("\nYou come across an abandoned campfire in a clearing. What do you do?")
        print("1. Search the camp for useful items.")
        print("2. Rest at the campfire.")
        print("3. Leave the area without disturbing anything.")

        choice = input("Enter your choice (1-3): ")
        match choice:
            case "1":
                print("You find a hidden pouch containing coins and a small trinket!")
                found_coins = random.randint(3, 10)
                print(f"Coins: {player.coins} + {found_coins}")
                player.coins += found_coins
                sleep(5)
                Game.dragon_encounter(player)

            case "2":
                print("You rest at the campfire and recover some health.")
                health_recovery = random.randint(5, 15)
                player.health += health_recovery
                print(f"Health: {player.health}")
                sleep(5)
                Game.dragon_encounter(player)

            case "3":
                print("You leave the camp untouched and continue on your way.")
                sleep(3)
                Game.dragon_encounter(player)

            case _:
                print("Invalid choice. The campfire burns out as you hesitate.")


    @staticmethod
    def dragon_encounter(player: Player):
        clear_console()
        print("\nYou encounter a fearsome dragon! What do you do?")
        print("1. Attempt to fight the dragon.")
        print("2. Run away as fast as you can.")

        choice = input("Enter your choice (1-2): ")
        match choice:
            case "1":
                print("You brace yourself and prepare to fight the dragon by rolling a dice...")
                dice_roll = random.randint(1, 6)
                print(f"You rolled a {dice_roll}!")

                match dice_roll:
                    case 1 | 2:
                        print("The dragon defeats you in a single fiery breath. You have died!")
                        sleep(5)
                        player.alive = False
                        display_end_game_stats(player, False)

                    case 3 | 4:
                        damage_taken = random.randint(20, 50)
                        print(f"You barely escape the dragon, but you lose {damage_taken} health!")
                        player.health -= damage_taken
                        if player.health <= 0:
                            print("Unfortunately, your injuries were too severe, and you succumb to them.")
                            sleep(5)
                            player.alive = False
                            display_end_game_stats(player, False)
                        else:
                            sleep(5)
                            display_end_game_stats(player, True)

                    case 5 | 6:
                        reward_coins = random.randint(50, 100)
                        print("You defeat the dragon in an epic battle and find a treasure hoard!")
                        print(f"You earn {reward_coins} coins as a reward.")
                        player.coins += reward_coins
                        sleep(8)
                        display_end_game_stats(player, True)

            case "2":
                print("You run away, avoiding a potentially deadly encounter. You live to fight another day.")
                sleep(5)
                display_end_game_stats(player, True)

            case _:
                print("Invalid choice. The dragon roars in frustration as you hesitate.")


game = Game()