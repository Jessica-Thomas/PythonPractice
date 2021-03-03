# Step 1
# Ask the user for their name and the year they were born.
name = input("Hi! What is your name?  ")

while True:
    birth_year = input("In what year were you born?  ")
    try:
        birth_year = int(birth_year)
    except ValueError:
        continue
    else:
        break

# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.
current_year = 2021
current_age =  current_year - birth_year

twenty_five = (25 - current_age) + current_year
fifty = (50 - current_age) + current_year
seventy_five = (75 - current_age) + current_year
hundred = (100 - current_age) + current_year


# Step 3
# If they're already past any of these ages, skip them.

if twenty_five > current_year:
    print("YO {}. In {} you will be 25".format(name,twenty_five))
if fifty > current_year:
    print("YO {}. In {} you will be 50".format(name,fifty))
if seventy_five > current_year:
    print("YO {}. In {} you will be 75".format(name,seventy_five))
if hundred > current_year:
    print("YO {}. In {} you will be 100".format(name,hundred))