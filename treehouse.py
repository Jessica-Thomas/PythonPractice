 print("A")
 try:
     result = "test" + 5
     print("B")
 except ValueError:
     print("C")
 except TypeError:
     print("D")
 else:
     print("E")
 print("F")


 print("A")
 try:
     result = 5 + 5
     print("B")
 except ValueError:
     print("C")
 except TypeError:
     print("D")
 else:
     print("E")
 print("F")




-----------------------------------------

 def suggest(product_idea):
     if len(product_idea) < 3:
         raise ValueError("Idea should be more than 3 charaters")
    
     return product_idea + "inator"





-----------------------------------------

     """
 This is importing a function named `tweet` from a file
     that we unfortunately don't have access to change.

 You use it like so:
 >>> tweet("Hello this is my tweet")

 If the function cannot connect to Twitter,
     the function will raise a `CommunicationError`
 If the message is too long,
     the function will raise a `MessageTooLongError`
 """
 from twitter import (
     tweet,
     MessageTooLongError,
     CommunicationError,
 )

 message = input("What would you like to tweet?  ")
  Your code here

 try:
     tweet(message)
    
 except CommunicationError:
     print("An error occurred attempting to connect to Twitter. Please try again!")

 except MessageTooLongError as err:
     print("Oh no! Your message was too long ({})".format(err))



-----------------------------------------

 def check_lottery_number(num):
     lottery_numbers = [77, 24, 8, 18, 5, 64]

     if num in lottery_numbers:
         print(f'{num} is a winning number!')
     else:
         print(f'Try again, {num} is not a winning number.')

 check_lottery_number(3)





 Classes:
 Alright, it's time create your first class all on your own!

 Make a new class named Student. Give it an attribute name and put your own name, as a string, into the attribute.

 class Student:
     name = "Jessica"

 Now, create a variable named me and assign it an instance of Student().

 Then print() out the name attribute of your instance.


 class Student:
     name = "Jessica"

     me = Student()
     print(me.name)

 This class should look familiar!

 First, I need you to add a method named praise to the Student class. It should take the self argument. Then, inside the praise method, return a positive message about the student using the name attribute.

 As an example, it could say "You're doing a great job, Jacinta!" or "I really like your hair today, Michael!".

 Feel free to change the name attribute to your own name, too!

 class Student:
     name = "Jess"
    
     def praise(self):
         return("You're doing a great job {}".format(self.name))
        




-----------------------------------------

 Alright, I need you to make a new method named feedback. It should take self and an argument named grade. Methods take arguments just like functions do.

 Inside the feedback method, if grade is above 50, return the result of the praise method. If it's 50 or below, return the reassurance method's result.

 class Student:
     name = "Your Name"

     def praise(self):
         return "You inspire me, {}".format(self.name)

     def reassurance(self):
         return "Chin up, {}. You'll get it next time!".format(self.name)

     def feedback(self, grade):
         if grade > 50:
             return self.praise()
         return self.reassurance()


-----------------------------------------

 Our Student class is coming along nicely!

 I'd like to be able to set the name attribute at the same time that I create an instance. Can you add the code for doing that?

 Override the __init__ method by adding your own __init__ method to the Student class. Add self and name as arguments to the __init__ method. Inside of __init__, set self.name to the argument name.

class Student:
    name = "Jess"
    
    def __init__(self, name= "Kudakwashe", **kwarg):
        self.name = name

        for key, value in kwarg.items():
            setattr(self, key, value)

    def praise(self):
        return "You inspire me, {}".format(self.name)
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()


-----------------------------------------

OK, let's combine everything we've done so far into one challenge!

First, create a class named RaceCar. In the __init__ for the class, take arguments for color and fuel_remaining. Set these as attributes on the instance.

Also, add the **kwargs argument and use setattr to take any other keyword arguments that come in.
class RaceCar:
    def __init__(self, color, fuel_remaining, **kwarg):
        self.color = color
        self.fuel_remaining = fuel_remaining
        
        for key, value in kwarg.items():
            setattr(self, key, value)


Vrroom!
OK, now let's handle the racecar running laps. Add a laps attribute to the RaceCar class and set it to 0. Add a method named run_lap. It'll take a length argument. It should reduce the fuel_remaining attribute by the length argument multiplied by 0.125 (length * 0.125). Also, increment the laps attribute by 1 each time the run_lap method is called.

class RaceCar:
    laps = 0
    def __init__(self, color, fuel_remaining, **kwarg):
        self.color = color
        self.fuel_remaining = fuel_remaining
        
        for key, value in kwarg.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining -= length*0.125
        self.laps += 1


Great! One last thing.

In Python, attributes defined on the class, but not an instance, are universal. So if you change the value of the RaceCar's laps attribute, any instance of RaceCar that doesn't have laps set explicitly will have its value changed, too!

For example, right now, if we made a RaceCar instance named red_car, then set RaceCar.laps = 10, red_car.laps would then be set to 10 too!

To prevent this, be sure to set the laps attribute inside the __init__ method (it doesn't have to be a keyword argument, though). If you already did it, just hit that "run" button and you're good to go!

class RaceCar:
    def __init__(self, color, fuel_remaining, **kwarg):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0
        
        for key, value in kwarg.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining -= length*0.125
        self.laps += 1



I've made you a super-simple Inventory class that would let someone store items in it.

I need you to create a new class, SortedInventory that should be a subclass of Inventory (it inherits from Inventory).

You can just put pass in the body of your class for this step.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
        
class SortedInventory(Inventory):
    pass


Great! Now, let's override the add_item method. First, add an add_item method to your new SortedInventory class. It should also take an item argument. Inside your new add_item method, use super() to call add_item() and pass it item to make sure the item still gets added to the slots list.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)

Sorted inventories should be just that: sorted. Right now, we just add an item onto the slots list whenever our add_item method is called. In the SortedInventory's add_item method, use the list.sort() method to make sure the slots list gets sorted after an item is added.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        self.slots.sort()


-----------------------------------------

Add a _str_ method to the DreamCar class. In the method, return a string that states the dream car's make and model. The string should look like this: 'My dream car is a Ford Mustang.'

class DreamCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    # insert your code here
    def __str__(self):
        return "My dream car is a {} {}.".format(self.make, self.model)


This class should look familiar!

I need you to add __mul__ to NumString so we can multiply our number string by a number. Go ahead and add __rmul__, too.


class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
         return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)
    
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
      
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        self.value = self + other
        return self.value
# add your code below
    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        self.value = self * other
        return self.value

Now wrap it up by adding in __imul__, which does in-place multiplication. Be sure to update self.value!

class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
         return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)
    
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
      
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        self.value = self + other
        return self.value
# add your code below
    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        self.value = self * other
        return self.value

# add your code here
    def __imul__(self, other):
        self.value = self * other
        return self.value




Here is a class called Album that holds a list of songs. Add an _iter_ method to our Album class and use yield or yield from so the songs in our album can be iterated through.

class Album:
    def __init__(self):
        self.songs = []
    def add(self, song):
        self.songs.append(song)
    # insert your code here
    def __iter__(self):
        yield from self.songs

-----------------------------------------


Alright, time to subclass int.

Make a class named Double that extends int. For now, just put pass inside the class.

class Double(int):
    pass

Now override __new__. Create a new int instance from whatever is passed in as arguments and keyword arguments. Return that instance.

You should remove the pass.

class Double(int):
    def __new__(*args, **kwargs):
        return int.__new__(*args,**kwargs)

And, finally, double (multiply by two) the int that you created in __new__. Return the new, doubled value. For example, Double(5) would return a 10.

class Double(int):
    def __new__(*args, **kwargs):
        return 2 * int.__new__(*args,**kwargs)

-----------------------------------------
Now I want you to make a subclass of list. Name it Liar.

Override the __len__ method so that it always returns the wrong number of items in the list. For example, if a list has 5 members, the Liar class might say it has 8 or 2.

You'll probably need super() for this.

class Liar(list):
    
    def __len__(self):
        return super(Liar, self).__len__() + 2



-----------------------------------------
Below is a class called DreamVacation that holds a location and list of activities. Create a @classmethod called rome that will return a new DreamVacation instance with cls() with the following arguments: location = 'Rome' and activities list = ['visit the Colosseum', 'Eat gelato'].

Hint: The classmethod should take cls instead of self as an argument.

class DreamVacation:
    def __init__(self, location, activities):
        self.location = location
        self.activities = activities
    # insert your code here

    @classmethod
    def rome(cls):
        return cls('Rome', ['visit the Colosseum', 'Eat gelato'])


-----------------------------------------
Add a new property to the Rectangle class named area. It should calculate and return the area of the Rectangle instance (width * length).

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
 # insert your code here
    @property
    def area(self):
        return self.width * self.length

Let's add one more property to our Rectangle class. This time, add a perimeter property that returns the perimeter of the rectangle (length * 2 + width * 2).



class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
 # insert your code here
    @property
    def area(self):
        return self.width * self.length
    
    @property
    def perimeter(self):
        return (self.length*2) + (self.width*2)


-----------------------------------------
Create a new class named TicTacToe that inherits from Board and give it an __init__ method. Inside the __init__ of the TicTacToe class use super() to initialize a board with width and height each set to 3. When an instance of TicTacToe is created, it will result in a board that has the dimensions 3 x 3.

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))
 # insert your code here

class TicTacToe(Board):
    def __init__(self, width=3, height=3):
        super().__init__(width, height)

Let's make all Board instances iterable so we can loop through their cells attribute. Inside the Board class, define an __iter__ method that yields the cells. If you need help, refer back to the "Emulating Builtins" video.


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

    def __iter__(self):
        yield from self.cells
          
class TicTacToe(Board):
    def __init__(self, width=3, height=3):
        super().__init__(width, height) 


-----------------------------------------
We'd like to compare songs by their length, which is measured in whole seconds. Create an __int__ method that should return the length of the song. Then, create the following comparison methods: __eq__, __lt__, __gt__, __le__ and __ge__.

class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

 # insert your code here
    def __int__(self):
        return int(self.length)

    def __eq__(self, other):
        return int(self) == other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) >= other

    def __le__(self, other):
        return int(self) <= other




-----------------------------------------
Create a new class in dice.py named D20 that extends Die. It should automatically have 20 sides and will not need any arguments to create.

import random


class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)
        
    def __int__(self):
        return self.value
      
    def __add__(self, other):
        return int(self) + other
    
    def __radd__(self, other):
        return self + other

 # insert your code here

class D20(Die):
    def __init__(self, value=0):
        super().__init__(sides=20)

In the hands.py file import the D20 class from dice.py. Create a classmethod named roll. Since it is a classmethod, it will take cls as an argument. It will also take the number of dice as an argument. Inside the roll classmethod create a new instance of the Hand class and assign it to a variable. Append a D20 to your Hand equal to the number of dice given as an argument to the roll classmethod. Then return the Hand of D20s. For example, if Hand.roll(2) is called, it would return a list with two D20s inside.


from dice import D20

class Hand(list):

    def __init__(self, size=0, die_class=D20):
        super().__init__()
        for _ in range(size):
            self.append(die_class())

    @classmethod
    def roll(cls, size=2):
        return cls(size=size)

    @property
    def total(self):
        return sum(self)


-----------------------------------------

















