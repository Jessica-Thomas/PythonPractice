# attendees = ["Joe", "Jill", "Michelle"]
# print(attendees)
# items = len(attendees)
# print(items)


# attendees = ["Joe", "Jill", "Michelle"]
# attendees.append("Barak")
# attendees.extend(["George", "Kamala"])
# optional_attendees = ["Donald", "Melania"]
# potential_attendees = attendees + optional_attendees
# print("There are",len(potential_attendees), "potential attendees")


# attendees.extend(optional_attendees)

# Wishlist
# parts = [
#     "Motherboard",
#     "Processor",
#     "RAM",
#     "Harddrive"
# ]

# print("Most Important: {}".format(parts[1]))

# print("Parts:")
# for part in parts:
#     print("-" + part)


# def display_wishlist(display_name, wishes):
#     print(display_name + ":")
#     suggested_gift = wishes.pop(0)
#     print("====>", suggested_gift, "<====")
#     for part in parts:
#         print("* " + part)
#     print()

#     display_wishlist("Parts", parts)


# def display_wishlist(display_name, wishes):
#     print("====> Suggested gift:", wishes[0], "<=====") 
#     # Return a slice of the list from the 2nd element on...
#     for wish in wishes[1:]:
#         print("* " + wish)
#     print()


# continents = [
#     'Asia',
#     'South America',
#     'North America',
#     'Africa',
#     'Europe',
#     'Antarctica',
#     'Australia',
# ]
# # Your code here

# for continent in continents:
#     if continent[0] == "A": print("* " + continent)
#     # ^^Target continents where first letter is A


# turtles = [
#     "Michelangelo",
#     "Leonardo",
#     "Raphael",
#     "Donatello",
# ]

# def shredder(names):
#     if len(names) >= 1:
#         names[0] = "Bebop"

# shredder(turtles)

# for turtle in turtles:
#     print("* " + turtle)



# attendees = ["Joe", "Jill", "Michelle"]
# attendees.append("Barak")
# attendees.extend(["George", "Kamala"])
# optional_attendees = ["Donald", "Melania"]
# potential_attendees = attendees + optional_attendees
# print("There are",len(potential_attendees), "potential attendees")

# to_line = ", ".join(attendees)
# cc_line = ", ".join(optional_attendees)

# print("To:  " + to_line)
# print("Cc:  " + cc_line)

# jessicathomas@Jessicas-MacBook-Air PythonPractice % python3 lists.py
# There are 8 potential attendees
# jessicathomas@Jessicas-MacBook-Air PythonPractice % python3 -i lists.py 
# There are 8 potential attendees
# To:  Joe, Jill, Michelle, Barak, George, Kamala
# Cc:  Donald, Melania
# >>> to_line.split(", ")
# ['Joe', 'Jill', 'Michelle', 'Barak', 'George', 'Kamala']
# >>> 


musical_groups = [
    ["Ad Rock", "MCA", "Mike D."],
    ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"],
    ["Salt", "Peppa", "Spinderella"],
    ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"],
    ["Chuck D.", "Flavor Flav", "Professor Griff", "Khari Winn", "DJ Lord"],
    ["Axl Rose", "Slash", "Duff McKagan", "Steven Adler"],
    ["Run", "DMC", "Jam Master Jay"],

# Here is a multi-dimensional list of musical groups. The first dimension is group, the second is group members.
# Can you loop through each group and output the members joined together with a ", " comma space as a separator, please?

for group in musical_groups:
    print(", ".join(group))

# Awesome! Now I'd like to see only groups that are trios, you know 3 members.
# So can you please only print out the trios? It should still use the joined string format from task 1.

for group in musical_groups:
    if len(group) == 3:
        print(", ".join(group))