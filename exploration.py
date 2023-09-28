import random
import time
from items import alien_items
from loading import loading

class Exploration:
    directions = [
        {"name": "North"},
        {"name": "East"},
        {"name": "South"},
        {"name": "West"},
    ]

    def exploration(self):
        abc = ["A", "B", "C", "D"]

        input_string = f"\nWhat direction do you want to go:"

        for i, direction in enumerate(self.directions):
            input_string += f"\n{abc[i]}: {direction['name']}"

        option = input(input_string + "\n").lower()

        time.sleep(2)

        if option == "a":
            print(f"\nYou have decided to go to the {self.directions[0]['name']}.")

        elif option == "b":
            print(f"\nYou have decided to go to the {self.directions[1]['name']}.")

        elif option == "c":
            print(f"\nYou have decided to go to the {self.directions[2]['name']}.")

        elif option == "d":
            print(f"\nYou have decided to go to the {self.directions[3]['name']}.")

        else:
            print("\nThis is not an option!")
            self.exploration()

    def research(self, spaceship):
        loading(5)

        number = random.randint(0, 2)

        if number == 1:
            found_item = random.choice(alien_items)
            print(f"\nYou found the following item: {found_item['name']}.")
            alien_items.remove(found_item)
            inp = input("Type 'a' to pick up the item: ").lower()

            if inp.lower() == "a":
                time.sleep(3)

                spaceship.inventory.append(found_item["name"])
                if found_item["name"] != "Fuel can" and found_item["name"] != "Repair kit":
                    spaceship.score += found_item["value"]

                print(
                    f"\nThe following item has been added to your inventory: {found_item['name']}."
                )
                if found_item["name"] != "Fuel can" and found_item["name"] != "Repair kit":
                    print(
                        f"Your score has been increased with {found_item['value']} to {spaceship.score}."
                    )
                time.sleep(4)
                spaceship.DisplayStatus()
                time.sleep(4)
            else:
                print(
                    f"\nUnfortunately you skipped the item worth: {found_item['value']} points."
                )
                time.sleep(2)
        else:
            print("\nYou have found nothing. Try again.")

        time.sleep(3)
