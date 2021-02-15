import random

class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least two sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randint(1, sides)
        # makes us have at least 2 sides, value is a whole number, and makes sure the value is at least 1
    def __int__(self):
        return self.value

    def __eq__(self, other): 
        return int(self) == other
        # equals-- convert to int, compare to other values

    def __ne__(self, other):
        return int(self) != other
        # not equal-- convert to int, compare to other values

    def __gt__(self, other):
        return int(self) > other
        # greater than

    def __lt__(self, other):
        return int(self) < other
        # less than

    def __ge__(self, other):
        return int(self) > other or int(self) == other
        # greater than or equal to

    def __le__(self, other):
        return int(self) < other or int(self) == other
        # less than or equal to

    def __add__(self, other): 
        return int(self) + other

    def __radd__(self, other): 
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
        # creating a die that always has 6 sides -- change sides=# to change the number of sides on our die


