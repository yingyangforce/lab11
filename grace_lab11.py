#+---------------------------+
#| lab11.py - Isaiah Grace |
#+---------------------------+

import random

# Task 1 --- 

class Character:
    def __init__(self, name, dex, speed, health, weapon=None):
        self.name = name
        self.dex = dex
        self.speed = speed
        self.max_health = health
        self.health = health
        self.weapon = weapon

    def get_name(self):
        return self.name
    
    def swing(self):
        return random.randint(0, self.dex)
    
    def dodge(self):
        return random.randint(0, self.speed)

    def change_health(self, amount):
        self.health += amount
        if self.health < 0: self.health = 0
        if self.health > self.max_health: self.health = self.max_health
    
    def add_weapon(self, weapon):
        self.weapon = weapon

    def get_damage(self):
        return 1 if not self.weapon else self.weapon.get_damage()

# Task 2 ---

class Weapon:
    def __init__(self, type, max_damage):
        self.type = type
        self.max_damage = max_damage
    
    def get_damage(self):
        return random.randint(1, self.max_damage)

# Task 3 --- added Weapon data/fncs to Character class
# Task 4 --- added get_damage() to Character class

doug = Character("doug", 3, 4, 20)
doug.add_weapon(Weapon("whip", 12))

print(doug.get_damage())
