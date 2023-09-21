from sound import Sound
from combat import Combat
from spaceship import Spaceship
import time

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
