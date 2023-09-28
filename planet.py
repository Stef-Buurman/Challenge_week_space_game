import random
import time
from exploration import Exploration
from combat import Combat
from observation import Observation
from spying import Spying
from sound import Sound

class Planet:       
    def __init__(self):
        self.name = ""
        self.on_planet = False
        self.counter = 0
        
    def arrival(self):
        print(f"\nYou have arrived on planet {self.name}.")

    def departure(self):
        print(f"\nYou are leaving planet {self.name}.")
        self.name = "Earth"
    
    def leave(self, spaceship):
        spaceship.fuel -= 20
        if spaceship.fuel <= 0:
            Sound("Media\PowerDownAlarm.mp3", 14, False).play()
            print("\nTHE THANK IS EMPTY!!!")
            Sound("Media\EmptyThank.mp3", 16, False).play()
            spaceship.in_space = False
            spaceship.game_over = True
            time.sleep(10)
            return

        elif spaceship.fuel <=50:
            time.sleep(2)
            print("\n\033[38;5;9mYour fuel is running low!\033[0m")
            spaceship.DisplayStatus()

        time.sleep(3)
        number = random.randint(0, 2)
        if number == 0 or number == 2:
            print("\nThere is another spaceship which is approaching your location.")
            combat = Combat()
            combat.inCombatShips(spaceship)

    all_planets = [
    {
        "name": "Xenon", 
        "description": "Xenon is a desert planet with scorching temperatures and two suns."
    },
    {
        "name": "Zephyria", 
        "description": "Zephyria is a lush, forested world known for its colorful, floating flora."
    },
    {
        "name": "Pandora", 
        "description": "Pandora is a moon-like planet featuring bioluminescent forests and unique wildlife."
    },
    {
        "name": "Avalon", 
        "description": "Avalon is an icy planet with vast frozen oceans and towering crystalline structures."
    },
    {
        "name": "Nebulon", 
        "description": "Nebulon is a gas giant with swirling, multicolored storm systems."
    },
    {
        "name": "Orbitar", 
        "description": "Orbitar is a small, rocky planet located close to its sun with extreme temperature variations."
    },
    {
        "name": "Celestia", 
        "description": "Celestia is a planet covered in vast, glowing, floating islands."
    },
    {
        "name": "Quasar", 
        "description": "Quasar is a mysterious, energy-rich planet with portals to other dimensions."
    },
    {
        "name": "Aurora", 
        "description": "Aurora is a planet known for its stunning light displays in its polar regions."
    },
    {
        "name": "Nova", 
        "description": "Nova is a planet with a constantly changing landscape due to volcanic activity."
    },
    {
        "name": "Titanium", 
        "description": "Titanium is a metallic planet with a strong magnetic field."
    },
    {
        "name": "Helios", 
        "description": "Helios is a planet bathed in perpetual daylight, with a sun that never sets."
    }
]
    
    planet_activities = [
    {
        "name": "Exploration",
        "description": "Explore the planet and find new items for research."
    },
    {
        "name": "Combat",
        "description": "Engage combat with enemies and find items for research."
    },
    {
        "name": "Spying",
        "description": "Spy enemies and get intel for the operation."
    },
    {
        "name": "Observation",
        "description": "Seek interaction and observe the findings."
    }
]   

    def select_planet(self, spaceship):
        three_random_planets = random.sample(self.all_planets, 3)

        abc = ["A","B","C"]

        input_string = "\nChoose your planet to visit:"
            
        for i, planet in enumerate(three_random_planets):
            input_string += f"\n{abc[i]}: {planet['name']}: {planet['description']}"
        
        if spaceship.counter > 3:
            input_string += f"\nD: Earth: Go back to planet earth and complete the mission."

        spaceship.counter += 1
        
        option = input(input_string + "\n").lower()
         
        time.sleep(2)

        if option == "a":
            print(f"\nYou have chosen to visit planet {three_random_planets[0]['name']}.")
            self.all_planets.remove(three_random_planets[0])
            self.name = three_random_planets[0]['name']
            self.on_planet = True
            self.counter = 0
        
        elif option == "b":
            print(f"\nYou have chosen to visit planet {three_random_planets[1]['name']}.")
            self.all_planets.remove(three_random_planets[1])
            self.name = three_random_planets[1]['name']
            self.on_planet = True
            self.counter = 0
           
        elif option == "c":
            print(f"\nYou have chosen to visit planet {three_random_planets[2]['name']}.")
            self.all_planets.remove(three_random_planets[2])
            self.name = three_random_planets[2]['name']
            self.on_planet = True
            self.counter = 0

        elif option == "d" and spaceship.counter > 3:
            print(f"\nYou have chosen to go back to planet earth and complete the mission.")
            spaceship.in_space = False
        
        else:
            spaceship.counter -= 1
            print("\nThis is not an option")
            self.select_planet(spaceship)
            
    def select_activity_on_planet(self, spaceship):

        abc = ["A","B","C","D"]

        input_string = f"\nWhat do you want to do on planet {self.name}:"
            
        for i, planet in enumerate(self.planet_activities):
            input_string += f"\n{abc[i]}: {planet['name']}: {planet['description']}"
        
        if self.counter > 3:
            input_string += f"\nE: Return to spaceship: Go back to the spaceship and go to another planet."

            if spaceship.health < 50 and "Repair kit" in spaceship.inventory:
                input_string += f"\nF: Repair the spaceship: Go repair the damage to the spaceship."

                if spaceship.fuel < 50 and "Fuel can" in spaceship.inventory:
                    input_string += f"\nG: Refuel the spaceship."

            elif spaceship.fuel < 50 and "Fuel can" in spaceship.inventory:
                input_string += f"\nF: Refuel the spaceship."

        elif spaceship.health < 50 and "Repair kit" in spaceship.inventory:
            input_string += f"\nE: Repair the spaceship: Go repair the damage to the spaceship."

            if spaceship.fuel < 50 and "Fuel can" in spaceship.inventory:
                input_string += f"\nF: Refuel the spaceship."

        elif spaceship.fuel < 50 and "Fuel can" in spaceship.inventory:
            input_string += f"\nE: Refuel the spaceship."

        self.counter += 1

        option = input(input_string + "\n").lower()
        
        time.sleep(2)

        if option == "a":
            print(f"\nYou have chosen to {self.planet_activities[0]['description'].lower()}")
            explore = Exploration()
            explore.exploration()
            explore.research(spaceship)

        elif option == "b":
            print(f"\nYou have chosen to {self.planet_activities[1]['description'].lower()}")
            combat = Combat()
            combat.inCombatPlanet(spaceship)

        elif option == "c":
            print(f"\nYou have chosen to {self.planet_activities[2]['description'].lower()}")
            my_spy = Spying(self.name)
            my_spy.spy()
            my_spy.report_findings(spaceship)

        elif option == "d":
            print(f"\nYou have chosen to {self.planet_activities[3]['description'].lower()}")
            observation = Observation()
            observation.observation(spaceship, self.name)

        elif self.counter > 3:
            if option == "e":
                print(f"\nYou have chosen to go back to the spaceship and go to another planet.")
                self.on_planet = False
            elif spaceship.health < 50 and "Repair kit" in spaceship.inventory and option == "f":
                print(f"\nYou have chosen to repair your spaceship.")
                spaceship.repair()
            elif spaceship.fuel < 50 and "Fuel can" in spaceship.inventory and (option == "f" or option == "g"):
                print(f"\nYou have chosen to refuel your spaceship.")
                spaceship.refuel()
        elif spaceship.health < 50 and "Repair kit" in spaceship.inventory:
            if option == "e":
                print(f"\nYou have chosen to go repair the damage to the spaceship.")
                spaceship.repair()
            elif spaceship.fuel < 50 and "Fuel can" in spaceship.inventory and option == "f":
                print(f"\nYou have chosen to refuel your spaceship.")
                spaceship.refuel()
        elif spaceship.fuel < 50 and "Fuel can" in spaceship.inventory and option == "e":
            print(f"\nYou have chosen to refuel your spaceship.")
            spaceship.refuel()
        
        else:
            self.counter -= 1
            print("\nThis is not an option")
            self.select_activity_on_planet(spaceship)