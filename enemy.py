import time
import random
import string

class Enemy:
    def __init__(self):
        self.health = random.randrange(5, 26, 5)

    def getDamage(self, damageAmount):
        self.health -= damageAmount
        if self.health <= 0:
            print(f"The enemy has died following your excellent fighting skills.")
            return True
        else:
            print(f"You did {damageAmount} damage to the enemy.")
            print(f"He still has {self.health} health left.")
            return False
    
    def attack(self, spaceship):
        # char = random.choice(string.ascii_letters + string.digits)
        # inputChar = input(f"FAST, TYPE THE KEY {char.lower()}")
        spaceship.RandomDamage()