import time
import random
from enemy import Enemy

class Combat:
    def __init__(self):
        self.enemy = Enemy()
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

    def inCombat(self, spaceship):
        print("\nYou engage a small group of weird looking aliens targeting you.")
        choise = input(
            "A: You dodge the first attacks  \nB: You go in with full charge damaging the spaceship \n"
        )
        time.sleep(2)
        if choise.lower() == "a":
            print("\nYou dodged the first attacks, now you can attack them.")
        elif choise.lower() == "b":
            spaceship.RandomDamage()

        enemiesDied = False
        while enemiesDied == False:
            enemiesDied = self.attack()
            if enemiesDied == True:
                break
            self.enemy.attack(spaceship)


    def attack(self):
        attacks = random.sample(self.space_attacks, 3)
        # print("Choose your attack!:")
        alph = ["A","B","C"]
        inputString = "\nChoose your attack!:"
        for i,att in enumerate(attacks):
            inputString += f"\n{alph[i]}: {att['name']}: {att['description']}" 
        attChoise = input(inputString + "\n")
        time.sleep(2)
        if attChoise.lower() == "a":
            print(f"\nYou used {attacks[0]['name']}")
            return self.enemy.getDamage(attacks[0]['damage'])
        elif attChoise.lower() == "b":
            print(f"\nYou used {attacks[1]['name']}")
            return self.enemy.getDamage(attacks[1]['damage'])
        elif attChoise.lower() == "c":
            print(f"\nYou used {attacks[2]['name']}")
            return self.enemy.getDamage(attacks[2]['damage'])