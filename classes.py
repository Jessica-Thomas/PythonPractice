import random

class Wizard:
    bearded = True
    powerful = True
    gray = True
    sneaky = False


class Thief:
    sneaky = True
    
    def pickpocket(self):
        if self.sneaky:
            return bool(random.randint(0, 1))
        return False

    def hide(self, light_level):
        return self.sneaky and light_level < 10


