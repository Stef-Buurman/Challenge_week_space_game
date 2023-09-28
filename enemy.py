import sys
import time
import random
import string
from sound import Sound

sys.path.append("Libraries\inputimeout")
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred


class Enemy:
    def __init__(self, ship):
        if ship:
            self.health = random.randrange(20, 66, 5)
        else:
            self.health = random.randrange(9, 36, 5)

    def getDamage(self, damageAmount):
        if random.randrange(1, 5) == 3:
            print("O no, the enemy dodged your attack!")
            time.sleep(1)
            return False
        else:  
            self.health -= damageAmount
            if self.health <= 0:
                Sound("Media\EnemyDied.mp3", 2, False).play()
                time.sleep(1)
                print(f"The enemy has died following your excellent fighting skills.")
                time.sleep(3)
                return True
            else:
                if random.randint(0, 7) % 2 == 1:
                    Sound("Media\DamageDone1.mp3", 2, False).play()
                else:
                    Sound("Media\DamageDone2.mp3", 2, False).play()
                print(f"You did {damageAmount} damage to the enemy.")
                print(f"He still has {self.health} health left.")
                return False

    def attack(self, spaceship):
        char = random.choice(string.ascii_letters + string.digits)
        inpString = f"\nFAST, type '{char.lower()}': "
        timeout = random.randrange(1, 4)

        try:
            inp = inputimeout(prompt=inpString, timeout=timeout)
            if char.lower() != inp.lower():
                inp = False
                print("\nYou dodged right into the attack of the enemy!")
                time.sleep(1.5)
                spaceship.RandomDamage(True)
                time.sleep(3)
        except TimeoutOccurred:
            print("\nYou were too late to dodge the attack!")
            inp = False
            time.sleep(1.5)
            spaceship.RandomDamage(True)
            time.sleep(3)

        if inp != False:
            print("\nGood job, you dodged the attack and have no damage.")

        try:
            inp = inputimeout(prompt="", timeout=1)
        except TimeoutOccurred:
            inp = inp
