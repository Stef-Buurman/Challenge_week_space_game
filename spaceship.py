from sound import Sound
import random
import time
class Spaceship:
    def __init__(self, name):
        self.userName = name
        self.fuel = 100
        self.health = 100
        self.inventory = ["Repair kit", "Sword"]
        self.score = 0

    def DisplayStatus(self):
        print(f"\n{self.userName}'s Status:")
        print(f"Fuel: {self.fuel}")
        print(f"Health: {self.health}")
        print(f"Inventory:{', '.join(self.inventory)}")

    def RandomDamage(self, notDodgable = False):
        if notDodgable == True:
            damage = random.randrange(1, 10)
        else:
            damage = random.randrange(0, 10)
        self.health -= damage
        if damage == 0:
            print("\nYou are lucky this time, you had no damage from the attack.")
        elif self.health <= 0:
            Sound("Media\GameOver.mp3", 17, False).play()
            print("\n\n\nYou died...")
            time.sleep(17)
        else:
            Sound("Media\DamageGotten.mp3", 2, False).play()
            print(f"\nYou got {damage} of damage.")
        time.sleep(2)
        self.DisplayStatus()
    
    def Repair(self):
        if self.health == 100:
            print("\nYou're ship is already in the best state, you cannot use any repair kit.")
        elif "Repair kit" in self.inventory:
            print("\nYou are using your repair kit...")
            time.sleep(2)
            self.health = 100
            self.inventory.remove("Repair kit")
            print("\nYou used your repair kit and are ready to go!")
            time.sleep(2)
            self.DisplayStatus()
        else:
            print("You don't have a repair kit so you cannot repair your ship!")
            print("You can find them by fighting aliens or exploring planets.")
            time.sleep(5)