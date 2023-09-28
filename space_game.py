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
        "\033[92mTeam:\033[0m Your task is to collect 1000 points while gathering information about space and extraterrestrial life and return with everything alive."
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

    time.sleep(5)
    if spaceship.score >= 1000:
        print(f"\033[94mYou:\033[0m This is {spaceship.userName} from the space mission. Do you read me?")
        time.sleep(5)
        
        print(f"\n\033[92mTeam:\033[0m Loud and clear, {spaceship.userName}! We've been anxiously awaiting your return. Did you complete the mission successfully?")
        time.sleep(5)

        print(f"\033[94mYou:\033[0m It's a success! I've collected a wealth of data about space and made some fascinating discoveries related to extraterrestrial life.")
        time.sleep(5)

        print(f"\n\033[92mTeam:\033[0m That's fantastic, {spaceship.userName}! We can't wait to hear all the details. You're in for quite the debriefing. How are you feeling after your solo journey?")
        time.sleep(5)

        print(f"\033[94mYou:\033[0m It's been an incredible experience, and I can't wait to share what I've learned with the world. Returning to Earth is a surreal feeling.")
        time.sleep(5)

        print(f"\033[94mYou:\033[0m My re-entry and landing systems are all green. I'm set to initiate re-entry, and if all goes according to plan, I'll touch down in the designated recovery area. All the samples and data are securely stored and should remain intact.")
        time.sleep(5)
        
        print(f"\n\033[92mTeam:\033[0m That's reassuring, {spaceship.userName}. We're ready to have the recovery team standing by to welcome you back. You've made history as a solo explorer, and your discoveries will reshape our understanding of the universe.")
        time.sleep(5)
        
        print(f"\033[94mYou:\033[0m Thank you. It's been an honor to embark on this solo mission. I can't wait to share my findings and insights with the world. Bringing back a piece of the cosmos with me feels surreal.")
        time.sleep(5)

        print(f"\n\033[92mTeam:\033[0m We'll be counting the minutes until your safe return, {spaceship.userName}. Get ready to make history once you're back on Earth, and we'll see you on the other side.")
        time.sleep(5)

        print(f"\033[94mYou:\033[0m You can count on it. See you soon. Over and out.")
        time.sleep(5)

    else:
        print(f"\033[94mYou:\033[0m This is {spaceship.userName} from the space mission. Do you read me?")
        time.sleep(5)
        
        print(f"\n\033[92mTeam:\033[0m Loud and clear, {spaceship.userName}! We've been anxiously awaiting your return. Did you complete the mission successfully?")
        time.sleep(5)
        
        print("\033[94mYou:\033[0m No, I couldn't find much, but I hope what I have is helpful.")
        time.sleep(5)

        print(f"\n\033[92mTeam:\033[0m That's unfortunate, {spaceship.userName}.")
        time.sleep(5)

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
    game_over1 = """
  ____    _    __  __ _____    _____     _______ ____ """
    game_over2 = """
 / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \ """
    game_over3 = """
| |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) | """
    game_over4 = """
| |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ < """
    game_over5 = """
 \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\ """
    
    background.stop()
    background = Sound("Media\YouDiedBackground.mp3", 17, False).play()
    Sound("Media\GameOver.mp3", 17, False).play()
    print("\n\n\nYou died...")
    for i in sorted(list(range(1, 11))):
        print("\n")
        time.sleep(1)
    try:
        print(game_over1, end="")
        time.sleep(1)
        print(game_over2, end="")
        time.sleep(1)
        print(game_over3, end="")
        time.sleep(1)
        print(game_over4, end="")
        time.sleep(1)
        print(game_over5, end="")
        time.sleep(1)

        inputimeout(prompt="\n\n\nEnter any key to exit: ", timeout=216)
    except TimeoutOccurred:
        print("")


background = Sound("Media\Background.mp3", 0, True)
spaceship = intro(background)
start = startAdventure(spaceship, background)
