import random
import time
class Spaceship:
    def __init__(self, name):
        self.userName = name
        self.fuel = 100
        self.health = 100
        self.inventory = ["Repair kit"]

    def DisplayStatus(self):
        print(f"\n{self.userName}'s Status:")
        print(f"Fuel: {self.fuel}")
        print(f"Health: {self.health}")
        print("Inventory:", ", ".join(self.inventory))

    def RandomDamage(self):
        damage = random.randrange(0, 10)
        self.health -= damage
        if damage == 0:
            print("\nYou are lucky this time, you had no damage from the attack.")
        else:
            print(f"\nYou got {damage} of damage.")
        self.DisplayStatus()
    
    def Repair(self):
        damage = random.randrange(0, 10)
        self.health -= damage
        if damage == 0:
            print("You are lucky this time, you had no damage from the attack.")
        else:
            print(f"You got {damage} of damage.")
        self.DisplayStatus()