import sys
from sound import Sound
from spaceship import Spaceship
from planet import Planet
import time
import os
from loading import loading

sys.path.append("Libraries\inputimeout")
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred


logo = """
 ____  ____   _    ____ _____    ____    _    __  __ _____ 
/ ___||  _ \ / \  / ___| ____|  / ___|  / \  |  \/  | ____|
\___ \| |_) / _ \| |   |  _|   | |  _  / _ \ | |\/| |  _|  
 ___) |  __/ ___ \ |___| |___  | |_| |/ ___ \| |  | | |___ 
|____/|_| /_/   \_\____|_____|  \____/_/   \_\_|  |_|_____| v1.00
"""

info = "A spatial adventure game, created by Stef and Nick."


def intro(background):
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    background.play()
    print(logo)
    print(info)
    print("\nWelcome to our beautiful Space Game!")
    player_name = input("Enter the name of your character: ")
    spaceship = Spaceship(player_name)
    print(
        f"\n\033[92mTeam:\033[0m Welcome {player_name}, you are the captain of the spaceship, so you are in charge."
    )
    print(
        "\033[92mTeam:\033[0m Your task is to find information about space and return with everything in one peace."
    )
    Sound("Media\Door.mp3", 7, False).play()
    time.sleep(9)
    return spaceship


def startAdventure(spaceship, background):
    print("\n\033[92mTeam:\033[0m Aircraft is ready to launch.")
    time.sleep(1)
    print("\033[92mTeam:\033[0m Let's get to business!")
    time.sleep(3)
    Sound("Media\countdown.mp3", 10, False).play()
    time.sleep(1.5)
    for i in sorted(list(range(1, 11)), reverse=True):
        print("\033[92mTeam:\033[0m " + str(i))
        time.sleep(1)
    print("LAUNCH!!!")
    spaceship.in_space = True
    Sound("Media\Launch.mp3", 5, False).play()
    time.sleep(5)

    planet = Planet()

    while spaceship.in_space == True and spaceship.game_over == False:
        planet.select_planet(spaceship)

        if spaceship.in_space == True:
            planet.leave(spaceship)
            if spaceship.game_over == True:
                break
            Sound("Media\Meteor.mp3", 8, False).play()
            loading(5)
            time.sleep(8)
            planet.arrival()
            time.sleep(3)

        while planet.on_planet == True and spaceship.game_over == False:
            planet.select_activity_on_planet(spaceship)

    if spaceship.game_over == True:
        game_over(background)
    else:
        planet.departure()
        loading(5)
        Sound("Media\Meteor.mp3", 8, False).play()
        time.sleep(8)
        planet.arrival()

        end(spaceship, background)


def end(spaceship, background):
    background.stop()
    background = Sound("Media\EndMusic.mp3", 0, True).play()

    print(
        f"\n\033[92mTeam:\033[0m Welcome back {spaceship.userName}, do you have enough information?"
    )
    time.sleep(3)
    if spaceship.score >= 1000:
        print("\033[94mYou:\033[0m Yeah I found a lot of stuff which can help us!")
    else:
        print(
            "\033[94mYou:\033[0m No I couldn't find much but I hope that what I have is useful."
        )

    for i in sorted(list(range(1, 11))):
        print("\n")
        time.sleep(1)
    print(f"Your score: {spaceship.score}")
    print(f"Your findings: {', '.join(spaceship.inventory)}")
    try:
        inputimeout(prompt="\n\n\nEnter any key to exit: ", timeout=216)
    except TimeoutOccurred:
        print("")


def game_over(background):
    background.stop()
    background = Sound("Media\YouDiedBackground.mp3", 17, False).play()
    Sound("Media\GameOver.mp3", 17, False).play()
    print("\n\n\nYou died...")
    for i in sorted(list(range(1, 11))):
        print("\n")
        time.sleep(1)
    try:
        inputimeout(prompt="\n\n\nEnter any key to exit: ", timeout=216)
    except TimeoutOccurred:
        print("")


background = Sound("Media\Background.mp3", 0, True)
spaceship = intro(background)
start = startAdventure(spaceship, background)
