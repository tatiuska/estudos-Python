from character import Hero, Enemy

hero = Hero(name="Hero", health=100)
enemy = Enemy(name="Enemy", health=100)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()
