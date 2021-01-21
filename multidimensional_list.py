# # MULTIDIMENDIONAL LISTS
# travel_expenses = [
#     [5.00, 2.75, 22.00, 0.00, 0.00],
#     [24.75, 5.50, 15.00, 22.00, 8.00],
#     [2.75, 5.50, 0.00, 29.00, 5.00],
# ]

# print("Travel Expenses:")
# week_number = 1
# for week in travel_expenses:
#     print("* Week #{}: ${}".format(week_number, sum(week)))
#     week_number += 1

# jessicathomas@Jessicas-MacBook-Air PythonPractice % python3 -i multidimensional_list.py
# Travel Expenses:
# * Week #1: $29.75
# * Week #2: $75.25
# * Week #3: $42.25
# >>> 



# Shopping List Application Requirements
# - as a user, i should be able to ask for help so i can understand how to use the application
# - as a user, i should be continually prompted so that i can add a grocery item or view my list when i need to
# - as a user, i should be able to add an item to the list
# - as a user, upon adding an item, i should know the total length of my list
# - as a user, i should be able to see the list at any time to verify my order
# - as a user, i should be able to state when i am done so i may print the total list

# Create a new empty list named shopping list
shopping_list = []

def show_help():
    print("What should we get at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to show your list.
    """)

# create a function named add_to_list that declares a parameter named item
    # add the item to the list
    # notify user an item was added and state the count
def add_to_list(item):
    shopping_list.append(item)
    print("Added! List has {} items".format(len(shopping_list)))


def show_list():
    print("Here is your grocery list:")
    for item in shopping_list:
        print(item)

show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()   
        continue

    # call add_to_list with new item as an argument
    add_to_list(new_item)
