import random
import characters


class Thief(Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))