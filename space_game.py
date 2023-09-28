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
    time.sleep(7)
    return spaceship


def startAdventure(spaceship, background):
    print("\n\033[92mTeam:\033[0m Aircraft is ready to launch.")
    time.sleep(0.5)
    print("\033[92mTeam:\033[0m Let's get to business!")
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

    while spaceship.in_space == True:
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

        while planet.on_planet == True:
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

    mission_passed1 = """ 
 __  __ ___ ____ ____ ___ ___  _   _   ____   _    ____ ____  _____ ____ """

    mission_passed2 = """
|  \/  |_ _/ ___/ ___|_ _/ _ \| \ | | |  _ \ / \  / ___/ ___|| ____|  _ \ """

    mission_passed3 = """
| |\/| || |\___ \___ \| | | | |  \| | | |_) / _ \ \___ \___ \|  _| | | | | """

    mission_passed4 = """
| |  | || | ___) |__) | | |_| | |\  | |  __/ ___ \ ___) |__) | |___| |_| | """

    mission_passed5 = """
|_|  |_|___|____/____/___\___/|_| \_| |_| /_/   \_\____/____/|_____|____/ """
        
        
    mission_failed1 = """
 __  __ ___ ____ ____ ___ ___  _   _   _____ _    ___ _     _____ ____ """

    mission_failed2 = """
|  \/  |_ _/ ___/ ___|_ _/ _ \| \ | | |  ___/ \  |_ _| |   | ____|  _ \ """

    mission_failed3 = """
| |\/| || |\___ \___ \| | | | |  \| | | |_ / _ \  | || |   |  _| | | | | """

    mission_failed4 = """
| |  | || | ___) |__) | | |_| | |\  | |  _/ ___ \ | || |___| |___| |_| | """

    mission_failed5 = """
|_|  |_|___|____/____/___\___/|_| \_| |_|/_/   \_\___|_____|_____|____/ """

    if spaceship.score >= 1000:
        print(mission_passed1, end="")
        time.sleep(1)
        print(mission_passed2, end="")
        time.sleep(1)
        print(mission_passed3, end="")
        time.sleep(1)
        print(mission_passed4, end="")
        time.sleep(1)
        print(mission_passed5, end="")
        time.sleep(1)
    else:
        print(mission_failed1, end="")
        time.sleep(1)
        print(mission_failed2, end="")
        time.sleep(1)
        print(mission_failed3, end="")
        time.sleep(1)
        print(mission_failed4, end="")
        time.sleep(1)
        print(mission_failed5, end="")
        time.sleep(1)

    print(f"\n\nYour score: {spaceship.score}")
    print(f"\nYour findings: {', '.join(spaceship.inventory)}")
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
