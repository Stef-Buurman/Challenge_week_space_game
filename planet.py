import random
import time

class Planet:       
    def __init__(self):
        self.name = ""
        
    def arrival(self):
        print(f"\nYou have arrived on planet {self.name}.")

    def departure(self):
        print(f"\nYou are leaving planet {self.name}.")

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
        "name": "Exploration/observation",
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
]   

    def select_planet(self):
        three_random_planets = random.sample(self.all_planets, 3)

        abc = ["A","B","C"]

        input_string = "\nChoose your planet to visit:"
            
        for i, planet in enumerate(three_random_planets):
            input_string += f"\n{abc[i]}: {planet['name']}: {planet['description']}"
        
        option = input(input_string + "\n").lower()
        
        time.sleep(2)

        if option == "a":
            print(f"You have chosen to visit planet {three_random_planets[0]['name']}.")
            self.all_planets.remove(three_random_planets[0])
            return three_random_planets[0]['name']
        
        elif option == "b":
            print(f"You have chosen to visit planet {three_random_planets[1]['name']}.")
            self.all_planets.remove(three_random_planets[1])
            return three_random_planets[1]['name']
        
        elif option == "c":
            print(f"You have chosen to visit planet {three_random_planets[2]['name']}.")
            self.all_planets.remove(three_random_planets[2])
            return three_random_planets[2]['name']
        
    def choose_activity(self):

        three_random_activities = random.sample(self.planet_activities, 3)

        abc = ["A","B","C"]

        input_string = f"\nWhat do you want to do in {self.name}?"
            
        for i, planet in enumerate(three_random_activities):
            input_string += f"\n{abc[i]}: {planet['name']}: {planet['description']}"
        
        option = input(input_string + "\n").lower()
        
        time.sleep(2)

        if option == "a":
            print(f"You have chosen the following activity: {three_random_activities[0]['name']}")
        
        elif option == "b":
            print(f"You have chosen the following activity: {three_random_activities[1]['name']}")
            
        elif option == "c":
            print(f"You have chosen the following activity: {three_random_activities[2]['name']}")
            
# Test     
# planet = Planet()
# planet.name = planet.select_planet()
# planet.arrival()
# planet.choose_activity()
# planet.departure()
