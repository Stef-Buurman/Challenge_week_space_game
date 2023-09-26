import sys
import time
import random
import string
from sound import Sound
sys.path.append('Libraries\inputimeout')
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred

class Enemy:
    def __init__(self, ship):
        if ship:
            self.health = random.randrange(20, 66, 5)
        else:
            self.health = random.randrange(5, 26, 5)

    def getDamage(self, damageAmount):
        self.health -= damageAmount
        if self.health <= 0:
            print(f"The enemy has died following your excellent fighting skills.")
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
        inpString = f"\nFAST, type the key '{char.lower()}'!"
        timeout = random.randrange(1, 4)
        
        try:
            inp = inputimeout(prompt=inpString, timeout=timeout)
            if char != inp:
                inp = False
                print("\nYou dodged right into the attack of the enemy!")
                time.sleep(1)
                spaceship.RandomDamage(True)
        except TimeoutOccurred:
            print("\nYou where too late to dodge the attack!")
            inp = False
            time.sleep(1)
            spaceship.RandomDamage(True)
        
        if inp != False:
            print("\nGood job, you dodged the attack and have no damage.")

# Enemy(False).attack(Spaceship("henk"))