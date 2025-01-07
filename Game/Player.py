import random

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

class Player:
    isAlive = True

    def __init__(self, name: str):
        self._name = name
        self._max_health = random.randint(50, 120)
        self._health = self._max_health
        self._damage = 10
        self._shield = random.uniform(0, 2)
        self._damage_multiplier = random.uniform(0.8, 2)

    def take_damage(self, damage: int):
        self._health -= damage

    def attack(self, target):
        target.health -= self._damage * self._damage_multiplier

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
        return self._damage_multiplier

    @property
    def damage(self):
        return self._damage

    @property
    def shield(self):
        return self._shield

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