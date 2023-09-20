from sound import Sound
import time

def intro(background):
    background.play()
    print("Welkom bij het o zo mooie SpacerGame")
    player_name = input("Vul hier de naam van je character in: ")
    print(f"\nWelkom {player_name}, jij bent een van de astronauten in een operatie om de ruimte te onderzoeken.")
    print("Jou doel is om zo veel mogelijk kennis te vergaren van de ruimte.")
    Alarm = Sound("Media\Alarm.mp3", 3, False).play()
    time.sleep(3)
    return player_name


background = Sound("Media\Background.mp3", 0, True)
player_name = intro(background)
