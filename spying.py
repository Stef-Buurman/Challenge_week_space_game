import random
import time

class Spying:
    def __init__(self, location):
        self.location = location
        self.findings = []

    def spy(self):
        print(f"\nSpying on aliens from {self.location}...")
        time.sleep(5)

        findings = []

        if random.random() < 0.3:
            findings.append("Detected alien radio signals.")
        
        if random.random() < 0.2:
            findings.append("Spotted a UFO in the sky.")
        
        if random.random() < 0.1:
            findings.append("Deciphered an alien language.")
        
        if random.random() < 0.15:
            findings.append("Found an alien artifact on the ground.")

        if random.random() < 0.25:
            findings.append("Observed an alien spaceship.")
        
        if random.random() < 0.2:
            findings.append("Detected mysterious energy readings.")
        
        if random.random() < 0.05:
            findings.append("Witnessed an alien abduction event.")
        
        if random.random() < 0.1:
            findings.append("Received a message from an extraterrestrial being.")

        if random.random() < 0.2:
            findings.append("Noticed crop circles in a nearby field.")
        
        if random.random() < 0.15:
            findings.append("Discovered a hidden alien base underground.")
        
        if random.random() < 0.1:
            findings.append("Encountered friendly aliens offering advanced technology.")
        
        if random.random() < 0.05:
            findings.append("Stumbled upon an intergalactic space portal.")

        if random.random() < 0.15:
            findings.append("Witnessed an alien dance party.")
        
        if random.random() < 0.2:
            findings.append("Found extraterrestrial flora and fauna.")
        
        if random.random() < 0.1:
            findings.append("Discovered an ancient alien civilization's ruins.")
        
        if random.random() < 0.05:
            findings.append("Saw an alien cooking show broadcast.")
        
        self.findings = findings

    def report_findings(self, spaceship):
        if not self.findings:
            print("\nNo alien findings to report.")
        else:
            print(f"\nAlien findings from {self.location}:")
            total = 0
            for finding in self.findings:
                print(f"- {finding}")
                time.sleep(1)
                number = random.randint(0, 10)
                total += number
                spaceship.score += number
            
            print(f"\nYour score has been increased with {total} to {spaceship.score}.")
            time.sleep(1)
            spaceship.DisplayStatus()
