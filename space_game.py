from sound import Sound
import time
import random

space_attacks = [
    {
        "name": "Plasma Cannon",
        "description": "Fire your ship's powerful plasma cannon at the alien fleet.",
        "damage": 10,
    },
    {
        "name": "Quantum Missiles",
        "description": "Launch a barrage of quantum missiles to devastate the alien mothership.",
        "damage": 15,
    },
    {
        "name": "Laser Turrets",
        "description": "Activate your ship's laser turrets to fend off swarming alien fighters.",
        "damage": 5,
    },
    {
        "name": "EMP Pulse",
        "description": "Deploy an EMP pulse to disrupt the aliens' energy shields and systems.",
        "damage": 10,
    },
    {
        "name": "Ion Cannon",
        "description": "Use the ion cannon to disable alien ships temporarily.",
        "damage": 5,
    },
    {
        "name": "Photon Torpedoes",
        "description": "Launch photon torpedoes for precise strikes against key alien targets.",
        "damage": 10,
    },
    {
        "name": "Solar Flare Beam",
        "description": "Unleash a solar flare beam to scorch alien ships with intense heat.",
        "damage": 15,
    },
    {
        "name": "Temporal Distortion",
        "description": "Trigger a temporal distortion field to slow down alien ships' movements.",
        "damage": 5,
    },
]

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


def inCombat(spaceship):
    print("\nYou engage a small group of weird looking aliens targeting you.")
    print("The aliens are agrassive and .")
    choise = input(
        "A: You dodge the first attacks  \nB: You go in with full charge damaging the spaceship \n:"
    )
    if choise == "A" or choise == "a":
        time.sleep(2)
        print("You dodged the first attacks, now you can attack them.")
    elif choise == "B" or choise == "b":
        spaceship.RandomDamage()

    attack()

    

def attack():
    attacks = random.sample(space_attacks, 3)
    # print("Choose your attack!:")
    alph = ["A","B","C"]
    inputString = "\nChoose your attack!:"
    for i,att in enumerate(attacks):
        inputString += f"\n{alph[i]}: {att['name']}: {att['description']}" 
    attChoise = input(inputString + "\n")
    time.sleep(2)
    # if attChoise == "A" or attChoise == "a":
    #     print(f"You used {attacks[0]['name']}")
    # elif attChoise == "B" or attChoise == "b":
    #     spaceship.RandomDamage()
    # elif attChoise == "C" or attChoise == "c":
        

background = Sound("Media\Background.mp3", 0, True)
spaceship = intro(background)
start = inCombat(spaceship)
