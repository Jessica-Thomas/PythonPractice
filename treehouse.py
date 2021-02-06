# print("A")
# try:
#     result = "test" + 5
#     print("B")
# except ValueError:
#     print("C")
# except TypeError:
#     print("D")
# else:
#     print("E")
# print("F")


# print("A")
# try:
#     result = 5 + 5
#     print("B")
# except ValueError:
#     print("C")
# except TypeError:
#     print("D")
# else:
#     print("E")
# print("F")





# def suggest(product_idea):
#     if len(product_idea) < 3:
#         raise ValueError("Idea should be more than 3 charaters")
    
#     return product_idea + "inator"





    
#     """
# This is importing a function named `tweet` from a file
#     that we unfortunately don't have access to change.

# You use it like so:
# >>> tweet("Hello this is my tweet")

# If the function cannot connect to Twitter,
#     the function will raise a `CommunicationError`
# If the message is too long,
#     the function will raise a `MessageTooLongError`
# """
# from twitter import (
#     tweet,
#     MessageTooLongError,
#     CommunicationError,
# )

# message = input("What would you like to tweet?  ")
# # Your code here

# try:
#     tweet(message)
    
# except CommunicationError:
#     print("An error occurred attempting to connect to Twitter. Please try again!")

# except MessageTooLongError as err:
#     print("Oh no! Your message was too long ({})".format(err))




def check_lottery_number(num):
    lottery_numbers = [77, 24, 8, 18, 5, 64]

    if num in lottery_numbers:
        print(f'{num} is a winning number!')
    else:
        print(f'Try again, {num} is not a winning number.')

check_lottery_number(3)