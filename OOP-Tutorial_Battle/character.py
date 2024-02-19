# Character class
class Character:
    # Class-level variables
    # race = "Human"

    def __init__(self, name: str, health: int, damage: int):
        # Object-level variables
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage

    # Method Attack
    def attack(self, target) -> None:
        target.health -= self.damage
        target.health = max(target.health, 0)
