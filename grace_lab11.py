#+---------------------------+
#| lab11.py - Isaiah Grace |
#+---------------------------+

import random

# Task 1 --- make Character class w/ member functions

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

# Task 2 --- make Weapon class

class Weapon:
    def __init__(self, type, max_damage):
        self.type = type
        self.max_damage = max_damage
    
    def get_damage(self):
        return random.randint(1, self.max_damage)

# Task 3 --- add Weapon data/fncs to Character class
# Task 4 --- add get_damage() to Character class

# Task 5 --- make 'em fight

doug = Character('doug', 5, 6, 20, Weapon('axe', 9))
biff = Character('biff', 9, 10, 18, Weapon('dagger', 6))

def interact(char1, char2):
    att1 = char1.swing()
    att2 = char2.swing()
    def1 = char1.dodge()
    def2 = char2.dodge()
    
    #Phase 1
    print(f"{char1.get_name()} is attacking {char2.get_name()}")
    
    if att1 > def2:
        print("Hit!")
        char2.change_health(att1 * -1)
    else:
        print("Miss.")
    
    if char2.health < 1:
        print(f"{char1.get_name()} vanquished {char2.get_name()}")
        return
    
    print()

    #Phase 2
    print(f"{char2.get_name()} is attacking {char1.get_name()}")

    if att2 > def1:
        char1.change_health(att2 * -1)
        print(f"Hit! [doug health: {doug.health}, biff health: {biff.health}]")
    else:
        print("Miss.")

    if char1.health < 1:
        print()
        print(f"{char2.get_name()} vanquished {char1.get_name()}")
        return
    
    print()

while (doug.health > 0) and (biff.health > 0):
    interact(doug, biff)
