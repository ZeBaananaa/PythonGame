import random
from Collectible import *

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

class Player:
    def __init__(self, name: str):
        self._name = name
        self._max_health = random.randint(50, 120)
        self._health = self._max_health - 20
        self._damage = 10
        self._shield = random.uniform(0, 2)
        self._damage_multiplier = random.uniform(0.8, 2)
        self._coins = random.randint(2, 10)
        self._alive = True
        self._inventory = []

    def __str__(self):
        return f"{self._name}: {self._health}/{self._max_health} HP"

    def take_damage(self, damage: int):
        self._health -= damage

    def attack(self, target):
        target.health -= self._damage * self._damage_multiplier

    def heal(self, amount):
        self._health += amount
        if self._health > self._max_health:
            self._health = self._max_health

    def add_item(self, item):
        if isinstance(item, Collectible):
            self._inventory.append(item)
            print(f"{item.name} was added to {self.name}'s inventory.")
        else:
            print("Only collectible items can be added to the inventory.")

    def remove_item(self, item_name):
        for item in self._inventory:
            if item.name == item_name:
                self._inventory.remove(item)
                print(f"{item_name} has been removed from {self.name}'s inventory.")
                return
        print(f"{item_name} isn't in the inventory.")

    def show_inventory(self):
        if not self._inventory:
            print(f"{self.name}'s inventory is empty.")
        else:
            print(f"{self.name}'s inventory :")
            for item in self._inventory:
                print(f"- {item.name} ({item.type})")

    ###########
    # Getters #
    ###########
    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def damage_multiplier(self):
        return round(self._damage_multiplier, 2)

    @property
    def damage(self):
        return round(self._damage, 2)

    @property
    def shield(self):
        return round(self._shield, 2)

    @property
    def alive(self):
        if self._health <= 0:
            return False
        else:
            return True

    @property
    def coins(self):
        return self._coins

    @property
    def final_damages(self):
        return self._damage * self._damage_multiplier

    @name.setter
    def name(self, value: str):
        self._name = value

    @health.setter
    def health(self, value: int):
        self._health = clamp(self._health + value, 0, self._max_health)

    @damage_multiplier.setter
    def damage_multiplier(self, value: int):
        self._damage_multiplier = value

    @damage.setter
    def damage(self, value: int):
        self._damage = value

    @shield.setter
    def shield(self, value: int):
        self._shield = value

    @alive.setter
    def alive(self, value):
        self._alive = value

    @coins.setter
    def coins(self, value: int):
        self._coins = value