import random
import time

class Exploration:
    directions = [
    {
        "name": "North"
    }, 
    {
        "name": "East"
    },
    {
        "name": "South"
    },
    {
        "name": "West"
    }
]
    items = [
    {
        "name": "Anti-Gravity Crystals", 
        "value": 42
    },
    {   
        "name": "Telepathic Plants", 
        "value": 17
    },
    {   
        "name": "Time-Warping Ores", 
        "value": 98
    },
    {   
        "name": "Cosmic Energy Stones", 
        "value": 73
    },
    {   
        "name": "Invisible Creatures", 
        "value": 55
    },
    {   
        "name": "Quantum Fog", 
        "value": 34
    },
    {   
        "name": "Bioluminescent Rivers", 
        "value": 61
    },
    {   
        "name": "Gravity-Defying Waterfalls", 
        "value": 29
    },
    {   
        "name": "Interdimensional Portals", 
        "value": 88
    },
    {   
        "name": "Mind-Reading Rocks", 
        "value": 12
    },
    {   
        "name": "Starfire Gemstones", 
        "value": 77
    },
    {
        "name": "Crystalized Dreams", 
        "value": 63
    }
]

    def exploration(self):

        abc = ["A","B","C","D"]

        input_string = f"\nWhat direction do you want to go:"
            
        for i, direction in enumerate(self.directions):
            input_string += f"\n{abc[i]}: {direction['name']}"
        
        option = input(input_string + "\n").lower()
        
        time.sleep(2)

        if option == "a":
            print(f"You have decided to go to the {self.directions[0]['name']}.")
        
        elif option == "b":
            print(f"You have decided to go to the {self.directions[1]['name']}.")

        elif option == "c":
            print(f"You have decided to go to the {self.directions[2]['name']}.")

        elif option == "d":
            print(f"You have decided to go to the {self.directions[3]['name']}.")

    def research(self, spaceship):
        time.sleep(3)
        
        number = random.randint(0, 2)
        
        if number == 1:
            found_item = random.choice(self.items)
            print(f"\nYou found the following item: {found_item['name']}.")

            inp = input("Type 'a' to pick up the item: ").lower()

            if inp.lower() == "a":
                spaceship.inventory.append(found_item["name"])
                spaceship.score += found_item["value"]
                
                print(
                    f"\nThe following item had been added to your inventory: {found_item['name']}."
                )
                print(
                    f"You score has been increased with {found_item['value']} to {spaceship.score}."
                )
            else:
                print(
                    f"\nUnfortunately you skipped the item worth: {found_item['value']} points."
                )
        else:
            print("You have found nothing. Try again.")
            
