import time
import random
from enemy import Enemy
from items import alien_items


class Combat:
    def __init__(self):
        self.enemyShip = Enemy(True)
        self.enemy = Enemy(False)

    spaceAttacksShips = [
        {
            "name": "Plasma Cannon",
            "description": "Fire your ship's powerful plasma cannon at the alien fleet.",
            "damage": 25,
        },
        {
            "name": "Quantum Missiles",
            "description": "Launch a barrage of quantum missiles to devastate the alien mothership.",
            "damage": 25,
        },
        {
            "name": "Laser Turrets",
            "description": "Activate your ship's laser turrets to fend off swarming alien fighters.",
            "damage": 15,
        },
        {
            "name": "EMP Pulse",
            "description": "Deploy an EMP pulse to disrupt the aliens' energy shields and systems.",
            "damage": 15,
        },
        {
            "name": "Ion Cannon",
            "description": "Use the ion cannon to disable alien ships temporarily.",
            "damage": 25,
        },
        {
            "name": "Photon Torpedoes",
            "description": "Launch photon torpedoes for precise strikes against key alien targets.",
            "damage": 30,
        },
        {
            "name": "Solar Flare Beam",
            "description": "Unleash a solar flare beam to scorch alien ships with intense heat.",
            "damage": 20,
        },
        {
            "name": "Temporal Distortion",
            "description": "Trigger a temporal distortion field to slow down alien ships' movements.",
            "damage": 15,
        },
    ]

    spaceAttacksPlanet = [
        {
            "name": "Slash",
            "damage": 5,
            "description": "Perform a swift and powerful slash with your sword.",
        },
        {
            "name": "Thrust",
            "damage": 10,
            "description": "Thrust your sword forward to pierce the enemy's defenses.",
        },
        {
            "name": "Spin Attack",
            "damage": 15,
            "description": "Execute a spinning attack, striking multiple foes in your path.",
        },
        {
            "name": "Counter Strike",
            "damage": 10,
            "description": "Defend against an enemy's attack and counter with a devastating strike.",
        },
        {
            "name": "Power Strike",
            "damage": 25,
            "description": "Charge up your sword for a powerful, high-damage strike.",
        },
        {
            "name": "Punch",
            "damage": 5,
            "description": "Deliver a strong punch to your opponent's face.",
        },
        {
            "name": "Kick",
            "damage": 10,
            "description": "Execute a powerful kick to your opponent's body.",
        },
        {
            "name": "Elbow Strike",
            "damage": 10,
            "description": "Strike your opponent with a sharp elbow jab.",
        },
        {
            "name": "Headbutt",
            "damage": 15,
            "description": "Lunge forward and headbutt your opponent with force.",
        },
        {
            "name": "Body Slam",
            "damage": 20,
            "description": "Lift your opponent and slam them onto the ground.",
        },
    ]

    def inCombatShips(self, spaceship):
        rand = random.randint(0, 6)
        if rand == 0:
            print(
                "\nYou encounter a spaceship which doesn't seem to be interested in combat."
            )
            print("The spaceship flees and cannot be stopped.")
            time.sleep(2)
            return
        elif rand == 1 or rand == 4 or rand == 6:
            print(
                "\nThe spaceship is aware of your existence but does not see you as a threat."
            )
        else:
            print(
                "\nThe spaceship is aware of your existence and instantly decides to start the attack."
            )
            time.sleep(3)
            self.enemy.attack(spaceship)

        time.sleep(5)
        enemiesDied = False
        while enemiesDied == False:
            enemiesDied = self.attackShips()
            if enemiesDied == True:
                self.drop_rand_item(spaceship)
                break
            time.sleep(1)
            self.enemyShip.attack(spaceship)
            time.sleep(2)

    def attackShips(self):
        attacks = random.sample(self.spaceAttacksShips, 3)
        alph = ["A", "B", "C"]
        inputString = "\nChoose your attack!:"
        for i, att in enumerate(attacks):
            inputString += f"\n{alph[i]}: {att['name']}: {att['description']}"
        attChoise = input(inputString + "\n")
        time.sleep(2)
        if attChoise.lower() == "a":
            print(f"\nYou used {attacks[0]['name']}")
            time.sleep(1)
            return self.enemyShip.getDamage(attacks[0]["damage"])
        elif attChoise.lower() == "b":
            print(f"\nYou used {attacks[1]['name']}")
            time.sleep(1)
            return self.enemyShip.getDamage(attacks[1]["damage"])
        elif attChoise.lower() == "c":
            print(f"\nYou used {attacks[2]['name']}")
            time.sleep(1)
            return self.enemyShip.getDamage(attacks[2]["damage"])

    def inCombatPlanet(self, spaceship):
        rand = random.randint(0, 2)
        if rand == 0:
            print("\nThe aliens still have no idea you're near them.")
        elif rand == 1:
            print(
                "\nThe aliens see you approaching but don't decide to start the attack."
            )
        else:
            print(
                "\nThe aliens see you approaching as threat and decide to start the attack."
            )
            time.sleep(3)
            self.enemy.attack(spaceship)
        time.sleep(5)
        enemiesDied = False
        while enemiesDied == False:
            enemiesDied = self.attackPlanet()
            if enemiesDied == True:
                self.drop_rand_item(spaceship)
                break
            self.enemy.attack(spaceship)

    def attackPlanet(self):
        attacks = random.sample(self.spaceAttacksPlanet, 3)
        alph = ["A", "B", "C"]
        inputString = "\nChoose your attack!:"
        for i, att in enumerate(attacks):
            inputString += f"\n{alph[i]}: {att['name']}: {att['description']}"
        attChoise = input(inputString + "\n")
        time.sleep(2)
        if attChoise.lower() == "a":
            print(f"\nYou used {attacks[0]['name']}")
            time.sleep(1)
            return self.enemy.getDamage(attacks[0]["damage"])
        elif attChoise.lower() == "b":
            print(f"\nYou used {attacks[1]['name']}")
            time.sleep(1)
            return self.enemy.getDamage(attacks[1]["damage"])
        elif attChoise.lower() == "c":
            print(f"\nYou used {attacks[2]['name']}")
            time.sleep(1)
            return self.enemy.getDamage(attacks[2]["damage"])

    def drop_rand_item(self, spaceship):
        if random.randint(0, 5) % 2 == 1:
            time.sleep(3)
            dropped_item = random.choice(alien_items)
            print(f"\nThe alien dropped the following item: {dropped_item['name']}.")
            alien_items.remove(dropped_item)
            inp = input("Type 'a' to pick up the item: ")
            if inp.lower() == "a":
                time.sleep(3)

                spaceship.inventory.append(dropped_item["name"])
                spaceship.score += dropped_item["value"]
                print(
                    f"\nThe following item has been added to your inventory: {dropped_item['name']}."
                )
                print(
                    f"Your score has been increased with {dropped_item['value']} to {spaceship.score}."
                )
                spaceship.DisplayStatus()
            else:
                print(
                    f"\nUnfortunately you skipped the item worth: {dropped_item['value']} points."
                )
