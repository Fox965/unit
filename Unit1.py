import random


class Unit:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, target):
        if type(self) == type(target):
            target.health -= random.randint(0, 100)



Units = [Unit('Юнит 1'), Unit('Юнит 2')]

while True:

    i = random.randint(0, 1)
    attacker, victim = Units[i], Units[i - 1]
    attacker.hit(victim)
    print(attacker.name, 'атаковал', victim.name,)
    print('У', victim.name, 'осталось здоровья', victim.health)
    if victim.health <= 0:
        print(attacker.name, 'победил!!!')
        break
