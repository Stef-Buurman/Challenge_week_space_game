import random
import time
from loading import loading

class Spying:
    def __init__(self, location):
        self.location = location
        self.findings = []

    all_findings = [
    "Detected alien radio signals.",
    "Spotted a UFO in the sky.",
    "Deciphered an alien language.",
    "Found an alien artifact on the ground.",
    "Observed an alien spaceship.",
    "Detected mysterious energy readings.",
    "Witnessed an alien abduction event.",
    "Received a message from an extraterrestrial being.",
    "Noticed crop circles in a nearby field.",
    "Discovered a hidden alien base underground.",
    "Encountered friendly aliens offering advanced technology.",
    "Stumbled upon an intergalactic space portal.",
    "Witnessed an alien dance party.",
    "Found extraterrestrial flora and fauna.",
    "Discovered an ancient alien civilization's ruins.",
    "Saw an alien cooking show broadcast.",
    "Encountered a telepathic alien species.",
    "Spotted an alien mothership in orbit.",
    "Discovered an alien time capsule with future technology.",
    "Observed a meeting between different alien species.",
    "Witnessed a celestial light show created by alien technology.",
    "Found a map leading to other extraterrestrial civilizations.",
    "Detected gravitational anomalies caused by nearby alien technology.",
    "Encountered a friendly alien pet.",
    "Received a tour of an alien city on another planet.",
    "Discovered an interdimensional rift created by alien experiments.",
    "Saw alien crop circles form in real-time.",
    "Encountered a group of aliens with advanced medical knowledge.",
    "Found an alien library containing knowledge of the universe.",
    "Witnessed an alien art exhibition in deep space.",
    "Discovered a holographic communication device left behind by aliens.",
    "Encountered a peaceful alien civilization on a distant planet.",
    "Discovered an alien trading post in a remote star system.",
    "Interacted with a hive mind alien species with shared consciousness.",
    "Witnessed an alien ritual celebrating the changing of seasons.",
    "Found an ancient alien artifact with unknown powers.",
    "Observed a massive alien migration across the galaxy.",
    "Detected an alien distress signal from a stranded spacecraft.",
    "Encountered a time-traveling alien historian studying Earth's history.",
    "Discovered a hidden alien research facility beneath an ocean.",
    "Witnessed a cosmic battle between rival alien factions.",
    "Found a mysterious alien garden with sentient plant life.",
    "Interacted with shape-shifting aliens who can mimic any form.",
    "Observed an alien species that communicates through dance.",
    "Detected an alien species with the ability to manipulate weather.",
    "Encountered an alien ambassador sent to establish diplomatic relations with Earth.",
    "Detected an alien space station hidden within an asteroid field.",
    "Witnessed an interstellar space race between different alien species.",
    "Discovered an ancient alien prophecy about Earth's destiny.",
    "Interacted with a peaceful intergalactic council of alien races.",
    "Found a mysterious alien artifact that can manipulate time.",
    "Observed a cosmic phenomenon where stars danced in intricate patterns.",
    "Encountered a nomadic alien tribe with unique cultural traditions.",
    "Detected a rogue planet that serves as a sanctuary for alien refugees.",
    "Stumbled upon a holographic archive of alien civilizations' histories.",
    "Witnessed an alien species that communicates through bioluminescent patterns.",
    "Found an alien craft capable of terraforming planets.",
    "Encountered a group of aliens researching Earth's ecosystems.",
    "Discovered an alien sports event that defies the laws of physics.",
    "Observed an alien species with the ability to manipulate gravity.",
    "Detected an extraterrestrial signal containing the secrets of the universe.",
]

    def spy(self):
        print(f"\nSpying on aliens from {self.location}...")
        
        loading(10)

        findings = []

        if random.random() < 0.2:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.15:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.1:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.15:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)

        if random.random() < 0.25:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.1:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.05:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.1:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)

        if random.random() < 0.2:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.15:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.1:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.05:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)

        if random.random() < 0.15:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.2:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.1:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        if random.random() < 0.05:
            random_item = random.choice(self.all_findings)
            self.all_findings.remove(random_item)
            findings.append(random_item)
        
        self.findings = findings

    def report_findings(self, spaceship):
        if not self.findings:
            print("\nNo alien findings to report.")
        else:
            print(f"\nAlien findings from {self.location}:")
            
            for finding in self.findings:
                print(f"- {finding}")
                time.sleep(1)
            
            self.inspect(spaceship)
    
    def inspect(self, spaceship):
        
        print(f"\nYou are reporting the findings you have found on {self.location}.")
        loading(10)
        input(f"\nType your documentation for spying on {self.location}: ")
        time.sleep(2)

        if f"{self.location} spying documentation" not in spaceship.inventory:
            print(f"\nAdded to inventory: {self.location} spying documentation")
            spaceship.inventory.append(f"{self.location} spying documentation")
        else:
            print(f"\nAdded findings to existing {self.location} spying documentation.")

        score = random.randrange(10, 150, 10)
        spaceship.score += score
        print(f"Your score has been increased with {score} to {spaceship.score}.")

        time.sleep(4)
        spaceship.DisplayStatus()
        time.sleep(4)