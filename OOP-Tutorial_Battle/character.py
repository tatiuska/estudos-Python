# Character class
from weapon import fists


class Character:
    # Class-level variables
    # race = "Human"

    def __init__(self, name: str, health: int):
        # Object-level variables
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    # Method Attack
    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)


class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)


class Enemy(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)