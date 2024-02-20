# creating a colored health bar
import os

os.system("")


class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red": "\033[91m",
                    "purple": "\33[95m",
                    "blue": "\33[34m",
                    "blue2": "\33[36m",
                    "blue3": "\33[96m",
                    "green": "\033[92m",
                    "green2": "\033[32m",
                    "brown": "\33[33m",
                    "yellow": "\33[93m",
                    "grey": "\33[37m",
                    "default": "\033[0m"}

    def __init__(self, entity, length: int = 20, is_colored: bool = True, color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.current_value = entity.health
        self.max_value = entity.health_max

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]
