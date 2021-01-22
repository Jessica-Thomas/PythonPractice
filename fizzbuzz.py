name = input("Please enter your name: ")
number = input("Please enter a number: ")

# TODO: Make sure the number is an integer
number = int(number)

# TODO: Define variables for is_fizz and is_buzz that stores 
# a Boolean value of the condition. Remember that the modulo operator, %, 
# can be used to check if there is a remainder.
fizz = number % 3 == 0
buzz = number % 5 == 0

# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************

if fizz and buzz:
    print(number, "is a FizzBuzz number.") 
elif fizz:
    print(number, "is a Fizz number.")  
elif buzz:
    print(number, "is a Buzz number.")
else:
    print(number, "is not Fizzy or Buzzy")


# Using the variables, check the condition of the value, and print the necessary
# string





















