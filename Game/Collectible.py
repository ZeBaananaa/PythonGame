from enum import Enum

class Collectible:
    class Type(Enum):
        HEAL = 0,
        USELESS = 1

    def __init__(self, name, collectible_type: str):
        self.name = name
        self.type = collectible_type

class HealingPotion(Collectible):
    def __init__(self, name, heal_amount):
        super().__init__(name, "HealingPotion")
        self.heal_amount = heal_amount

    def use(self, character):
        character.heal(self.heal_amount)
        print(f"{character.name} Has gained {self.heal_amount} hp!")