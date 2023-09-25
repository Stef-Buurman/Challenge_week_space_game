from sound import Sound
from combat import Combat
from spaceship import Spaceship
from planet import Planet
import time
import os


def intro(background):
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    # background.play()
    print("Welcome to the beautiful SpacerGame")
    player_name = input("Enter the name of you character: ")
    spaceship = Spaceship(player_name)
    print(
        f"\nWelcome {player_name}, you are the captain of the spaceship, so you are in charge."
    )
    print(
        "Your task is to find information about space and return with everthing in one peace."
    )
    # Sound("Media\Door.mp3", 7, False).play()
    # time.sleep(7)
    return spaceship

def startAdventure(spaceship):
    print("\n\033[92mTeam:\033[0m aircraft is ready to launch.")
    time.sleep(0.5)
    print("Let's get to business!")
    for i in sorted(list(range(1, 11)), reverse=True):
        print(i)
        time.sleep(1)
    print("LAUNCH!!!")
    Sound("Media\Launch.mp3", 5, False).play()
    time.sleep(5)
    planet = Planet()
    planet.select_planet()

background = Sound("Media\Background.mp3", 0, True)
spaceship = intro(background)
start = startAdventure(spaceship)
