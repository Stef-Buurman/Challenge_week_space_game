import random
import time

from loading import loading


class Observation:
    # def __init__(self):
    observation_options = [
        {
            "name": "Interaction",
            "description": "Try to interact with alienlike creatures and get information about how they live.",
        },
        {
            "name": "Inspect",
            "description": "Inspect the planet your currently on to get to know the planet and get to know the conditions.",
        },
        {
            "name": "Admire caves",
            "description": "Admire the cave systems on the planet and find information about any other creatures.",
        },
    ]

    space_creatures = [
        "Stellar Serpent",
        "Cosmic Phoenix",
        "Nebula Nymph",
        "Asteroid Albatross",
        "Lunar Lizard",
        "Galactic Gryphon",
        "Celestial Chimera",
        "Orbiting Owl",
        "Supernova Squirrel",
        "Satellite Scorpion",
        "Planetary Parrot",
        "Meteor Moth",
        "Comet Cobra",
        "Interstellar Iguana",
        "Astronomical Armadillo",
        "Starship Seahorse",
        "Astroquid",
        "Cosmic Chameleon",
        "Uranus Unicorn",
    ]

    def observation(self, spaceship, planet):
        abc = ["A", "B", "C"]

        input_string = f"\nWhat direction do you want to go:"

        for i, direction in enumerate(self.observation_options):
            input_string += f"\n{abc[i]}: {direction['name']}"

        option = input(input_string + "\n").lower()

        time.sleep(2)

        if option == "a":
            print(f"\nYou have decided to {self.observation_options[0]['name']}.")
            time.sleep(1)
            self.interactionChoise(spaceship)
        elif option == "b":
            print(f"\nYou have decided to {self.observation_options[1]['name']}.")
            time.sleep(1)
            self.inspect(spaceship, planet)
        elif option == "c":
            print(f"\nYou have decided to {self.observation_options[2]['name']}.")
            time.sleep(1)
            self.admire_caves(spaceship, planet)

    def interactionChoise(self, spaceship):
        number = random.randint(0, 2)
        if number == 0:
            self.interaction1(spaceship)
        elif number == 1:
            self.interaction2(spaceship)
        elif number == 2:
            self.interaction3(spaceship)

    def interaction1(self, spaceship):
        print(
            f"\033[94mYou:\033[0m (Through the intercom, looking out into the vastness of space) This view, Zara, it's breathtaking and yet, it can be so isolating."
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (Responding through a communication link) Indeed, {spaceship.userName}. Space can be a silent and lonely place, but it also holds the beauty of the unknown."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Staring in awe at the alien's appearance) I'm {spaceship.userName}, an astronaut from Earth. I never thought I'd meet intelligent life out here."
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (Smiling gently) Your presence here is a rarity, {spaceship.userName}. Your kind seldom ventures beyond its own celestial sphere."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Curious) Tell me about your world, Zara. It's so different from Earth."
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (Proudly) Orynthia is a planet of unity and harmony. We are connected to the land, the water, and the sky. Our purpose is to protect the balance of life."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Admiring) That sounds incredible. On Earth, we often struggle with maintaining that balance."
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (Thoughtful) Every world faces its challenges, {spaceship.userName}. It is the choices we make that define our destiny."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Reflective) You're right, Zara. We must take responsibility for our actions."
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (With empathy) Your journey here speaks of a yearning for knowledge. What do you seek, {spaceship.userName}?"
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Passionate) I seek understanding. We've always wondered if we're alone in the universe. Meeting you proves that we're not."
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (Wise) Knowledge is the bridge between worlds. It can illuminate the path to unity."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Curious) How do you communicate with each other on Orynthia?"
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (Raising a hand, a soft glow surrounds it) We communicate through energy, thoughts, and emotions, transcending words."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Amazed) That's remarkable. Our communication relies heavily on spoken language and technology."
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (Intrigued) Your world must be full of diverse languages and cultures."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Nods) Yes, Earth is a tapestry of languages, beliefs, and customs. Sometimes, it leads to misunderstandings."
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (Reflective) Diversity can be a source of strength or conflict. It depends on how it's embraced."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Grateful) Talking to you, Zara, is a privilege. I hope to share this experience with my fellow humans someday."
        )
        time.sleep(8)
        print(
            f"\033[38;5;205mZara\033[0m (Smiles) The universe is vast, {spaceship.userName}. Your journey has just begun."
        )
        time.sleep(6)
        self.interactionItem(spaceship, "Zara")

    def interaction2(self, spaceship):
        print(
            f"\033[94mYou:\033[0m (Speaking through your headset, awestruck by the cosmic panorama) Lyra, you won't believe the view from up here. It's like a dream."
        )
        time.sleep(8)
        print(
            f"\033[38;5;217mLyra\033[0m (Responding in a melodious, alien language, which {spaceship.userName} surprisingly understands) {spaceship.userName}, welcome to the realm of the stars. We've been watching your kind's journey for some time."
        )
        time.sleep(8)
        print(f"\033[94mYou:\033[0m (Surprised) You can understand me?")
        time.sleep(8)
        print(
            f"\033[38;5;217mLyra\033[0m (Nods) Your desire for communication resonates beyond words, {spaceship.userName}. It bridges gaps."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Humbled) I've always dreamed of this moment, meeting an intelligent alien species."
        )
        time.sleep(8)
        print(
            f"\033[38;5;217mLyra\033[0m (Curious) Tell me, {spaceship.userName}, what do you hope to find out here in the cosmos?"
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Looking at Earth from space) We're explorers, seekers of knowledge. But more than that, I think we're searching for meaning, a deeper connection to the universe."
        )
        time.sleep(8)
        print(
            f"\033[38;5;217mLyra\033[0m (Understanding) The quest for meaning is universal, transcending boundaries of worlds. We, too, seek to understand the purpose of our existence."
        )
        time.sleep(8)
        print(f"\033[94mYou:\033[0m (Amazed) How do you perceive the universe, Lyra?")
        time.sleep(8)
        print(
            f"\033[38;5;217mLyra\033[0m (Expressive) We sense it as a vast symphony, where every star and planet contributes a unique note, creating harmony through their interactions."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Thoughtful) That's a beautiful way to describe it. On Earth, sometimes we forget how interconnected everything is."
        )
        time.sleep(8)
        print(
            f"\033[38;5;217mLyra\033[0m (Empathetic) It's easy to lose sight of the interconnectedness, especially in the vastness of space. But every action has consequences that ripple through the cosmos."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Contemplative) I hope we can learn from our actions, become better stewards of our planet, and contribute positively to the cosmic symphony."
        )
        time.sleep(8)
        print(
            f"\033[38;5;217mLyra\033[0m (Supportive) The universe embraces growth and change. Your journey, {spaceship.userName}, is a testament to that."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Smiling) I'll carry this conversation with me, Lyra, and share it with Earth. Maybe we can find unity in our shared aspirations."
        )
        time.sleep(8)
        print(
            f"\033[38;5;217mLyra\033[0m (Warmly) Unity, {spaceship.userName}, is a powerful force in the cosmos."
        )
        time.sleep(6)
        self.interactionItem(spaceship, "Lyra")

    def interaction3(self, spaceship):
        print(
            f"\033[94mYou:\033[0m (Speaking through your helmet's communicator, floating in her spacesuit) This is incredible, Xanar. To think that I'm floating here in the cosmos."
        )
        time.sleep(8)
        print(
            f"\033[38;5;226mXanar\033[0m (Responding in a soft, melodious tone) Welcome, {spaceship.userName}. Space has a way of humbling even the most seasoned travelers."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Gazing at the distant stars) It's so vast, so full of wonder. I've dreamed of this moment my whole life."
        )
        time.sleep(8)
        print(
            f"\033[38;5;226mXanar\033[0m (Curious) Tell me, {spaceship.userName}, what drives your kind to explore the stars?"
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Reflecting) We're driven by curiosity, by the need to know what's out here. And maybe, deep down, it's a search for connection, a way to understand our place in the universe."
        )
        time.sleep(8)
        print(
            f"\033[38;5;226mXanar\033[0m (Nodding) Connection is a universal longing. We, too, seek to connect with other intelligent beings across the galaxies."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Intrigued) Have you met other travelers like me before?"
        )
        time.sleep(8)
        print(
            f"\033[38;5;226mXanar\033[0m (Thoughtful) Not often, but occasionally, beings from distant worlds pass through our corner of the universe. Each encounter is a gift."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Feeling a sense of unity) It's amazing how space can bring together beings from different worlds."
        )
        time.sleep(8)
        print(
            f"\033[38;5;226mXanar\033[0m (With a hint of sadness) Yet, it can also be a reminder of how fragile life is. The universe is a delicate tapestry of existence."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Empathetic) We've seen the same on Earth—how our actions impact the balance of life. It's a responsibility we mustn't take lightly."
        )
        time.sleep(8)
        print(
            f"\033[38;5;226mXanar\033[0m (Supportive) Indeed, {spaceship.userName}. Your kind has the potential to shape the cosmos in profound ways."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Looking back at Earth, a tear forming in her eye) I hope we can make the right choices, for our planet and for the universe."
        )
        time.sleep(8)
        print(
            f"\033[38;5;226mXanar\033[0m (Encouraging) The choices you make today ripple through the fabric of time. Let them be ones that bring harmony and understanding."
        )
        time.sleep(8)
        print(
            f"\033[94mYou:\033[0m (Feeling inspired) I'll carry this conversation with me, Xanar. It's a reminder of the unity we can find in the cosmos."
        )
        time.sleep(8)
        print(
            f"\033[38;5;226mXanar\033[0m (Warmly) Safe travels, {spaceship.userName}. May your journey be filled with discovery and wisdom."
        )
        time.sleep(8)
        self.interactionItem(spaceship, "Xanar")

    def interactionItem(self, spaceship, alienName):
        print(f"\nYou are documenting the information gotten from {alienName}")
        loading(5)
        print(f"\nAdded to inventory: Alien documentation")
        spaceship.score += random.randrange(0, 150, 10)
        spaceship.inventory.append(f"Alien documentation")
        number = random.randint(0, 3)
        if number == 2:
            time.sleep(2)
            print(f"\nYou recieved a gift from {alienName}.")
            spaceship.score += random.randrange(50, 200, 20)
            spaceship.inventory.append(f"Alien gift")

        time.sleep(2)
        spaceship.DisplayStatus()

    def inspect(self, spaceship, planet):
        print(f"\nYou are inspecting the place you currently are on {planet}")
        loading(10)
        input(f"\nType your documentation of {planet}: ")
        time.sleep(2)
        print(f"\nAdded to inventory: {planet} documentation")
        spaceship.score += random.randrange(10, 150, 10)
        spaceship.inventory.append(f"{planet} documentation")
        time.sleep(2)
        spaceship.DisplayStatus()

    def admire_caves(self, spaceship, planet):
        print(f"\nYou are admiring the caves found on {planet}")
        loading(10)
        time.sleep(1)
        number = random.randint(0, 5)
        if number == 1:
            creature_name = random.choice(self.space_creatures)
            print(f"\nYou found a creature named {creature_name}")
        elif number == 4:
            print("You found a creature without a name.")
            creature_name = input("How would you name the creature?: ")

        if number == 1 or number == 4:
            time.sleep(2)
            input(f"\nType your documentation of planet: {planet} and creature: {creature_name}: ")
            time.sleep(2)
            print(f"\nAdded to inventory: {planet} documentation, {creature_name} documentation")
            spaceship.score += random.randrange(10, 150, 10)
            spaceship.inventory.append(f"{planet} documentation")
            spaceship.inventory.append(f"{creature_name} documentation")
        else:
            time.sleep(2)
            input(f"\nType your documentation of planet: {planet}: ")
            time.sleep(2)
            print(f"\nAdded to inventory: {planet} documentation")
            spaceship.score += random.randrange(10, 150, 10)
            spaceship.inventory.append(f"{planet} documentation")
        time.sleep(2)
        spaceship.DisplayStatus()
