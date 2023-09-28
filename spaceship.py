from sound import Sound
import random
import time

class Spaceship:
    def __init__(self, name):
        self.userName = name
        self.fuel = 100
        self.health = 10
        self.inventory = ["Repair kit", "Fuel can", "Sword"]
        self.score = 0
        self.in_space = False
        self.counter = 0
        self.game_over = False

    def DisplayStatus(self):
        print(f"\n{self.userName}'s Status:")
        print(f"Health: {self.health}")
        print(f"Fuel: {self.fuel}")
        print(f"Score: {self.score}")
        print("Inventory:", ", ".join(self.inventory))

    def RandomDamage(self, notDodgable = False):
        if notDodgable == True:
            damage = random.randrange(1, 10)
        else:
            damage = random.randrange(0, 10)
        self.health -= damage
        if damage == 0:
            print("\nYou are lucky this time, you had no damage from the enemy attack.")
        elif self.health <= 0:
            self.game_over = True
        else:
            Sound("Media\DamageGotten.mp3", 2, False).play()
            time.sleep(2)
            print(f"\nYou got {damage} damage from the enemy attack.")
            time.sleep(2)
            self.DisplayStatus()
    
    def repair(self):
        if self.health == 100:
            print("\nYour ship is already in the best state, you cannot use a repair kit.")
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
        