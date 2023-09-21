from sound import Sound
from combat import Combat
import time
import random

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

def intro(background):
    # background.play()
    print("Welcome to the beautiful SpacerGame")
    player_name = input("Enter the name of you character: ")
    spaceship = Spaceship(player_name)
    print(
        f"\nWelcome {player_name}, you are the captain of the spaceship, so you are in charge."
    )
    print(
        "Your task is to find information about space and return with everting in one peace."
    )
    # Alarm = Sound("Media\Alarm.mp3", 3, False).play()
    # time.sleep(10)
    return spaceship

def startAdventure(spaceship):
    combat = Combat()
    combat.inCombat(spaceship)
        

background = Sound("Media\Background.mp3", 0, True)
spaceship = intro(background)
start = startAdventure(spaceship)
