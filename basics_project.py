# requirements:
# - get user's name
# - have errors reported in a friendly manner
# - output how many tickets are left using tickets_remaining variable 
# - allow user to request certain numerof tix
# - calculate the price -- tix X TICKET_PRICE, assign to variable
# - allow user to confirm order
# - do not offer tickets that aren't available
# - let people know when there are no more tickets left 
# - be able to purchase using credit and bitcoin
# - add a service charge to each transaction

TICKET_PRICE = 10
SERIVCE_CHARGE = 2

tickets_remaining = 100

#created function to 
def calculated_price(num_tix):
    return (num_tix * TICKET_PRICE) + SERIVCE_CHARGE

#run continuously until we run out of tickets
while tickets_remaining >= 1:
    # print("There are",tickets_remaining,"tickts left") 
    # OR 
    print("There are {} tickts available.".format(tickets_remaining))
    name = input("What is your name?  ")
    num_tix = input("Hi {}, how many tickets would you like to buy?  ".format(name))
    
    #expect a ValueError to happen d/t invalid input
    #raise a ValueError if asking for more tickets than available
    try:
        num_tix = int(num_tix)
        if num_tix > tickets_remaining:
            raise ValueError("Oh no! There are {} tickets available.".format(tickets_remaining))

    except ValueError as err:
        print("Oh no. We ran into an error. {}.".format(err))
    else:
        cost = calculated_price(num_tix)
        proceed = input("{} tickets will cost you ${}. Would you like to proceed with your ${} order, {}?  Yes or no?  ".format(num_tix,cost,cost,name))

        if proceed.lower() == "yes":
            print("Sold! {} tickets are yours!".format(num_tix))
            tickets_remaining = (tickets_remaining - num_tix)

        # if proceed.lower() == "no":
        #     OR 
        else:
            print("Bummer! Feel free to come back if you change your mind!")

print("Tickets are all sold out!")




continents = [
'Asia',
'South America',
'North America',
'Africa',
'Europe',
'Antarctica',
'Australia',
]
# Your code here

for continent in continents:
if continent[0] == "A": print("* " + continent)


