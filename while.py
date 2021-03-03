# Problem 1: Warm the oven
# Write a while loop that checks to see if the oven
# is 350 degrees. If it is, print "The oven is ready!"
# If it's not, increase current_oven_temp by 25 and print
# out the current temperature.

current_oven_temp = 75

while current_oven_temp < 350:
    current_oven_temp += 25
    print(current_oven_temp)
else:
    print("The oven is ready.")

# Solution 1 here

# Problem 2: Total and average
# Complete the following function so that it asks for
# numbers from the user until they enter 'q' to quit.
# When they quit, print out the list of numbers,
# the sum and the average of all of the numbers.

def total_and_average():
    numbers = []
    while True:
        num = input("Give me a number, or 'q' to quit:  ").lower()
        if num == 'q':
            break
        try:
            numbers.append(float(num))
        except ValueError:
            continue

    # ignores anything not a number or q
    print("You gave me the following numbers: ", numbers)
    print("The total is: ", sum(numbers))
    print("The average is: ", sum(numbers)/len(numbers))

total_and_average()
