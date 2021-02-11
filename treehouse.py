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




------------------
 def suggest(product_idea):
     if len(product_idea) < 3:
         raise ValueError("Idea should be more than 3 charaters")
    
     return product_idea + "inator"





------------------
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



------------------
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
        




------------------
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


------------------
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


------------------
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











