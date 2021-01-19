# this is SIMPLE

# password = input("Please enter the password:  ")
# while password != "hotchocolate":
#     password = input("Wrong. Try again:   ")

# print("Welcome to the thunder dome, bitch.")


# adding in a second check, to allow a limited number of attempts
import sys

MASTER_PASSWORD = "hotchocolate"
password = input("Please enter the password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many failed attempts. Sucks to suck.")
    password = input("Wrong. Try again:   ")
    attempt_count += 1
    # attempt count +1
print("Welcome to the thunder dome, bitch.")