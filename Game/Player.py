class Player:
    isAlive = True

    def __init__(self, name: str, health: int, strength: int):
        self.name = name
        self.health = health
        self.strength = strength