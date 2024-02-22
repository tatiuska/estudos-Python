# Classe Armor
from weapon import Weapon

class Armor:
    material: str
    defense: int
    name: str

    def equip(self, weapon: Weapon) -> int:
        return self.defense - weapon.damage

        

# métodos: equipar, dropar e defender