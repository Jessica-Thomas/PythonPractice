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
Add a docstring to Treehouse.student. It should say "Gives a pleasant message about the student.".

class Treehouse:
    def student(self, name):
        """Gives a pleasant message about the student."""
        return '{} is a great Treehouse student!'.format(name)

Becomes: 

class Treehouse:
    def student(self, name):
        """Gives a pleasant message about the student."""
        return '{} is a great Treehouse student!'.format(name)



Add a docstring to Treehouse. Should be "Methods related to Treehouse and students.".

class Treehouse:
    def student(self, name):
        """Gives a pleasant message about the student."""
        return '{} is a great Treehouse student!'.format(name)


Becomes: 

class Treehouse:
    """Methods related to Treehouse and students."""
    def student(self, name):
        """Gives a pleasant message about the student."""
        return '{} is a great Treehouse student!'.format(name)

-----------------------------------------
Task 1
Log a message with a level of DEBUG. The message can say anything you want.

import logging

logging.basicConfig(filename='cc.log', level=logging.DEBUG)

# Write your code below here

logging.debug('Debug message')


Task 2
Log "The French have the Grail" as a WARNING level message.

import logging

logging.basicConfig(filename='cc.log', level=logging.DEBUG)

# Write your code below here

logging.debug('Debug message')

logging.warning('The French have the Grail')


-----------------------------------------
Import PDB and call set_trace() where it's needed.

def something_silly(arg1, arg2):
    if len(arg1) > len(arg2):
        # Import and use PDB here
        import pdb; pdb.set_trace()
        arg1[0] = arg2[0]
    return arg1, arg2

-----------------------------------------

Challenge Task 1 of 4
Import the datetime library.

import datetime

Challenge Task 2 of 4
Create a variable named now that holds the results of datetime.datetime.now().

import datetime

now = datetime.datetime.now()

Challenge Task 3 of 4
Create a new variable called two that holds the value of now with the hour set to 14. Use the .replace() method.

import datetime

now = datetime.datetime.now()

two = now.replace(hour=14)


Challenge Task 4 of 4
Finally, change two so its minute is 30.

import datetime

now = datetime.datetime.now()

two = now.replace(hour=14, minute=30)

-----------------------------------------
Challenge Task 1 of 1
Write a function called far_away that takes one argument, a timedelta. Add that timedelta to datetime.datetime.now() and return the resulting datetime object.

import datetime
def far_away(timeDelta):
  return datetime.datetime.now() + timeDelta



-----------------------------------------
Write a function named minutes that takes two datetimes and, using timedelta.total_seconds() to get the number of seconds, returns the number of minutes, rounded, between them. The first will always be older and the second newer. You'll need to subtract the first from the second.

import datetime
time_1 = datetime.datetime.now()
time_2 = datetime.datetime.now().replace(minute=59)

def minutes(time_1, time_2):
    delta = time_2 - time_1
    delta_seconds = delta.total_seconds()
    return round(delta_seconds/60)

-----------------------------------------
Create a function named to_string that takes a datetime and gives back a string in the format "24 September 2012".

import datetime

def to_string(datetime_arg):
    return datetime_arg.strftime('%d %B %Y')

Create a new function named from_string that takes two arguments: a date as a string and an strftime-compatible format string, and returns a datetime created from them.

import datetime

def to_string(datetime_arg):
    return datetime_arg.strftime('%d %B %Y')

def from_string(datetime_str, datetime_str_format):
    return datetime.datetime.strptime(datetime_str, datetime_str_format)

-----------------------------------------
Write a function named time_tango that takes a date and a time. It should combine them into a datetime and return it.

import datetime

def time_tango(date, time):
    return datetime.datetime.combine(date, time)


-----------------------------------------
Write a function named delorean that takes an integer. Return a datetime that is that many hours ahead from starter.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def delorean(ahead):
    return starter.replace(hour=starter.hour+ahead)


-----------------------------------------
Write a function named time_machine that takes an integer and a string of "minutes", "hours", "days", or "years". This describes a timedelta. Return a datetime that is the timedelta's duration from the starter datetime.


import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def time_machine(integer, string):
    if string == 'years':
        string = 'days'
        integer *= 365
    return starter + datetime.timedelta(**{string: integer})


-----------------------------------------
Create a function named timestamp_oldest that takes any number of POSIX timestamp arguments. Return the oldest one as a datetime object.

Remember, POSIX timestamps are floats and lists have a .sort() method.

import datetime

def timestamp_oldest(*args):
    return datetime.datetime.fromtimestamp(min(args))


-----------------------------------------
Challenge Task 1 of 3
Create a variable named moscow that holds a datetime.timezone object at +4 hours.

import datetime 
moscow = datetime.timezone(datetime.timedelta(hours=4))

Challenge Task 2 of 3
Now create a timezone variable named pacific that holds a timezone at UTC-08:00.

import datetime 
moscow = datetime.timezone(datetime.timedelta(hours=4))
pacific = datetime.timezone(datetime.timedelta(hours=-8))


Challenge Task 3 of 3
Finally, make a third variable named india that hold's a timezone at UTC+05:30.

import datetime 
moscow = datetime.timezone(datetime.timedelta(hours=4))
pacific = datetime.timezone(datetime.timedelta(hours=-8))
india = datetime.timezone(datetime.timedelta(hours=+5.5))


-----------------------------------------
Challenge Task 1 of 2
naive is a datetime with no timezone.

Create a new timezone for US/Pacific, which is 8 hours behind UTC (UTC-08:00).

Then make a new variable named hill_valley. Copy the datetime info from naive and add the tzinfo attribute with the US/Pacific timezone you made.


import datetime

naive = datetime.datetime(2015, 10, 21, 4, 29)
pacific = datetime.timezone(datetime.timedelta(hours=-8))
hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)


Challenge Task 2 of 2
Great, but the tzinfo attribute just sets the timezone, it doesn't move the datetime to the new timezone. Let's move one.

Make a new timezone that is UTC+01:00 and set it to a variable called tz.

Create a new variable named paris that uses hill_valley and the astimezone() method to change hill_valley to the new timezone.


import datetime

pacific = datetime.timezone(datetime.timedelta(hours=-8))
europe = datetime.timezone(datetime.timedelta(hours=+1))
naive = datetime.datetime(2015, 10, 21, 4, 29)
hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)
paris = hill_valley.astimezone(europe)

-----------------------------------------
Challenge Task 1 of 2
starter is a naive datetime. Use pytz to make it a "US/Pacific" datetime instead and assign this converted datetime to the variable local.

Challenge Task 2 of 2
Now create a variable named pytz_string by using strftime with the local datetime. Use the fmt string for the formatting.

import datetime
import pytz

fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)

pacific = pytz.timezone('US/Pacific')
local = pacific.localize(starter)
pytz_string = local.strftime(fmt)


-----------------------------------------
Create a function named to_timezone that takes a timezone name as a string. Convert starter to that timezone using pytz's timezones and return the new datetime.

import datetime

import pytz

starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(arg):
    timezone = pytz.timezone(arg)
    return starter.astimezone(timezone)


-----------------------------------------
Challenge Task 1 of 5
Use open() to load the file "basics.txt" into the variable file_object.

with open("basics.txt") as file_object:
    data = file_object.read()


Challenge Task 2 of 5
Read the contents of file_object into a new variable named data.
with open("basics.txt") as file_object:
    data = file_object.read()


Challenge Task 3 of 5
Now close the file_object file so it isn't taking up memory.

with open("basics.txt") as file_object:
    data = file_object.read()  
    file_object.close()

Challenge Task 4 of 5
Import re. Create an re.match() for the word "Four" in the data variable. Assign this to a new variable named first.

import re

with open("basics.txt") as file_object:
    data = file_object.read()
    file_object.close()

    first = re.match(r'Four', data)

Challenge Task 5 of 5
Finally, make a new variable named liberty that is an re.search() for the word "Liberty" in our data variable.

import re

with open("basics.txt") as file_object:
    data = file_object.read()
    file_object.close()

    first = re.match(r'Four', data)
    liberty = re.search(r'Liberty', data)


-----------------------------------------
Challenge Task 1 of 2
Write a function named first_number that takes a string as an argument. The function should search, with a regular expression, the first number in the string and return the match object.

import re

def first_number(strings):
  data = re.search(r'\d', strings)
  return data


Challenge Task 2 of 2
Now, write a function named numbers() that takes two arguments: a count as an integer and a string. Return an re.search for exactly count numbers in the string. Remember, you can multiply strings and integers to create your pattern.

For example: r"\w" * 5 would create r"\w\w\w\w\w".

import re

def first_number(strings):
  data = re.search(r'\d', strings)
  return data

def numbers(count, user_string):
      return re.search(r'\d' * count, user_string)


-----------------------------------------
Challenge Task 1 of 1
Create a function named phone_numbers that takes a string and returns all of the phone numbers in the string using re.findall(). The phone numbers will all be in the format 555-555-5555.

import re

def phone_numbers(str1): 
    return (re.findall(r'\d{3}?-\d{3}-\d{4}', str1))


-----------------------------------------
Challenge Task 1 of 1
Create a function named find_words that takes a count and a string. Return a list of all of the words in the string that are count word characters long or longer.

import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

def find_words(count, string):
    return re.findall(r'\w{'+ str(count) + ',}', string)

-----------------------------------------
Challenge Task 1 of 1
Create a function named find_emails that takes a string. Return a list of all of the email addresses in the string.

import re

# Example:
# >>> find_email("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk")
# ['kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk']

def find_emails(string): 
  re_string = re.findall(r'[-\w\d+.]+@[-\w\d.]+', string)
  return re_string

-----------------------------------------
Challenge Task 1 of 1
Create a variable named good_numbers that is an re.findall() where the pattern matches anything in string except the numbers 5, 6, and 7.

import re

string = '1234567890'
good_numbers = re.findall(r'[^567]', string)

-----------------------------------------

Challenge Task 1 of 1
Create a variable names that is an re.match() against string. The pattern should provide two groups, one for a last name match and one for a first name match. The name parts are separated by a comma and a space.

import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'([\w]*), ([\w]+ [\w]+)', string)

-----------------------------------------
Challenge Task 1 of 2
Create a new variable named contacts that is an re.search() where the pattern catches the email address and phone number from string. Name the email pattern email and the phone number pattern phone. The comma and spaces * should not* be part of the groups.

import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    ^[\w]+,\s[\w]+,\s
    (?P<email>[\w+.]*@[\w.]*)
    ,\s
    (?P<phone>\d{3}-\d{3}-\d{4})
    ,\s
    @[\w]+$
''', string, re.X|re.I|re.M)



Challenge Task 2 of 2
Great! Now, make a new variable, twitters that is an re.search() where the pattern catches the Twitter handle for a person. Remember to mark it as being at the end of the string. You'll also want to use the re.MULTILINE flag.

import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
    ^[\w]+,\s[\w]+,\s
    (?P<email>[\w+.]*@[\w.]*)
    ,\s
    (?P<phone>\d{3}-\d{3}-\d{4})
    ,\s
    @[\w]+$
''', string, re.X|re.I|re.M)

twitters = re.search(r'''
    @[\w]+$
''', string, re.X|re.M)

-----------------------------------------
Challenge Task 1 of 2
Create a variable named players that is an re.search() or re.match() to capture three groups: last_name, first_name, and score. It should include re.MULTILINE.  

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
  (?P<last_name>[\w ]*)
  ,\s
  (?P<first_name>[\w ]*)
  :\s
  (?P<score>[\d]*)
''', string, re.X | re.M)


Challenge Task 2 of 2
Wow! OK, now, create a class named Player that has those same three attributes, last_name, first_name, and score. I should be able to set them through __init__.

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search(r'''
  (?P<last_name>[\w ]*)
  ,\s
  (?P<first_name>[\w ]*)
  :\s
  (?P<score>[\d]*)
''', string, re.X | re.M)

class Player:
    def __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score


-----------------------------------------
Now I need you to write a function named absolute that takes two arguments, a path string and a root string. If the path is not already absolute, return the path with the root prepended to it.

For example: absolute("projects/python_basics/", "/") would return "/projects/python_basics/" while absolute("/home/kenneth/django", "C:\") would return "/home/kenneth/django".

def absolute(path, root):
    if(not os.path.isabs(path)):
        new_path = ''.join((root, path))
        return new_path
    else:
        return path


-----------------------------------------
Challenge Task 1 of 1
Create a function named dir_contains takes a path to a directory and a list of file names. If all of the file names exist within that directory, return True, otherwise, return False.

import os

def dir_contains(dir_path, file_names):
    dir_files = list(os.listdir(dir_path))
    for file_name in file_names:
        if file_name not in dir_files:
            return False
    return True

-----------------------------------------
Challenge Task 1 of 1
Create a function named create_daily_dir in backup.py. This function should take a string which will be a date in either year-month-day (2012-12-22) or month-day-year (12-22-2012) format. Use that to create a directory like 2012-12-22 (year-month-day) in the financial directory (which is in the current directory).

This means that by calling create_daily_dir("04-22-2017"), we'd have a directory structure like financial/2017-04-22/.

import os

def create_daily_dir(string):
    if int(string.split("-")[2]) > 31:
        new_str = string.split("-")[2] + '-' + string.split("-")[0] + '-' + string.split("-")[1]
    else:
        new_str = string
    os.makedirs('financial/' + new_str, exist_ok=True)

-----------------------------------------
Challenge Task 1 of 1
Finish the function named cleanup in consistency.py. This function should take a string which will be a path to a local directory. The file names in this directory are messy. I need you to clean them up so they all follow the same pattern. Examples and further explanation are in the comments in the file below.

import os

# Filenames consist of a username (alphanumeric, 3-12 characters)
# and a date (four digit year, two digit month, two digit day),
# and an extension. They should end up in the format
# year-month-day-username.extension.

# Example: kennethlove2-2012-04-29.txt becomes 2012-04-29-kennethlove2.txt

def cleanup(path):
    for f in os.scandir(path):
        if f.is_file():
            f = f.path.split('/')[1]
            filename = f.split('.')[0]
            extension = f.split('.')[1]
            date = []
            for _ in filename.split('-'):
                try:
                    int(_)
                    date.append(_)
                except ValueError:
                    username = _
            old_name = path + '/' + f
            new_name = path + '/' + '-'.join(date) + '-' + username + '.' + extension
            os.rename(old_name, new_name)


-----------------------------------------
Challenge Task 1 of 2
Make a function named delete_by_date. It should take date string like 2015-10-31 and delete any files in the "backups" local directory that have that date in their filename.

Just like the last challenge, the files will be named in the format "year-month-day-username.extension".


import os

def delete_by_date(date):
    for f in os.listdir(os.getcwd() + '/backups'):
        if date in f:
            os.remove('backups/' + f)


Challenge Task 2 of 2
Now create a second function named delete_by_user that works similarly but deletes files that have a particular username in their filename.

import os

def delete_by_date(date):
    for f in os.listdir(os.getcwd() + '/backups'):
        if date in f:
            os.remove('backups/' + f)
            
def delete_by_user(username):
    for f in os.listdir(os.getcwd() + '/backups'):
        if username in f:
            os.remove('backups/' + f)
            

-----------------------------------------
Challenge Task 1 of 1
I'd like you to change how get_root works. I still want to ask for a path but if the path is relative, change it into an absolute path. You can assume that the path is relative from the current working directory. The function should always return an absolute path.

import pathlib


def get_root():
    root = pathlib.PurePath(
        input("What's the full path where you'd like the project? ")
    )
    if not root.is_absolute():
        return get_root()
    return root

BECOMES:
import os
import pathlib

def get_root():
    root = pathlib.PurePath(
        input("What's the full path where you'd like the project? ")
    )
    if not root.is_absolute():
        dirname = os.path.dirname(__file__)
        root = os.path.join(dirname, root)
    return root

-----------------------------------------
Challenge Task 1 of 1
This challenge is a bit different from others you've probably done, so try to approach it with an open, creative mind.

I made a slugify function in the last video, but that is just one approach to making a slug. I want you to make your own slugify function in slug.py. Your function should accept two arguments, a string to make into an acceptable file or directory name, and a path.

The rules? Slugs should be unique for their path (you can't have two files or directories with the same name in the same directory), slugs shouldn't have spaces in them, and slug should start with a number, letter, or underscore. Other than that, it's up to you!

import re
import os

def slugify(string, path):
    if not re.match(r'[\w\d_]', string):
        string += '_'
    string = re.sub(r'\s+', '_', string)
    slug = os.path.join(path, string)
    while os.path.exists(slug):
        slug += '_'
    return slug


-----------------------------------------
Challenge Task 1 of 1
Add a doctest to average() that tests the function with the list [1, 2]. Because of how we test doctests, you'll need to leave a blank line at the end of your doctest before the closing quotes.

def average(num_list):
    """Return the average for a list of numbers"""
    return sum(num_list) / len(num_list)


Becomes:


def average(num_list):
    '''Return the average for a list of numbers

    >>> average([1, 2])  # <-- added space after prompt
    1.5

    '''
    return sum(num_list) / len(num_list)


-----------------------------------------

lets see if i fixed the permission issue i created 






