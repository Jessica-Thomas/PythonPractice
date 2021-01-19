# import math

# def split_check(total,people):
#     cost_per_person = math.ceil(total / people)
#     return cost_per_person
# #math.ceil rounds up to a whole number so we don't get 5 decimal places
# #calling split_check and storing in amount_due

# total_due = float(input("What is the check total?  "))
# people = int(input("How many people are splitting the check?  "))
# amount_due = split_check(total_due, people)


# print("Each person owes ${}".format(amount_due))

# EXCEPTIONS-- try code

import math

def split_check(total,people):
    if people <= 1:
        raise ValueError("More than 1 person required to split check.")
    cost_per_person = math.ceil(total / people)
    return cost_per_person

try:
    total_due = float(input("What is the check total?  "))
    people = int(input("How many people are splitting the check?  "))
    amount_due = split_check(total_due, people)
except ValueError as err:
        print("That is not a valid value. Please enter a number.") 
        print("({})".format(err))
else:  
 
    print("Each person owes ${}".format(amount_due))