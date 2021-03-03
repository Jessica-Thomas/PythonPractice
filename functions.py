# -------
praise = "You are crushing it"
praise = praise.upper()
numberofcharacters = len(praise)
result = praise + "!" * numberofcharacters
print(result)
# gives us number of exclamation points equal to number of characters in praise variable


advice = "Don't forget to ask for help"
advice = advice.upper()
numberofcharacters = len(advice)
result = advice + "!" * (numberofcharacters // 2)
print(result)

advice2 = "Don't repeat yourself. Keep things DRY"
advice2 = advice2.upper()
numberofcharacters = len(advice2)
result = advice2 + "!" * (numberofcharacters // 2)
print(result)
# -------------- Repetitive, garbage route to take. Below defines a function that does the same as above but is significantly cleaner

def yell(text):
    text = text.upper()
    numberofcharacters = len(text)
    result = text + "!" * (numberofcharacters // 4)
    print(result)

yell("You are crushing it")
yell("Don't forget to ask for help")
yell("Don't repeat yourself. Keep things DRY")





#Treehouse quiz question-- start of a word guessing game
# def display_blanks( word):
#     blanks = "-" * len(word)
#     print(blanks)

# print("Puzzle 1:")
# display_blanks("treehouse")
# print("Puzzle 2:")
# display_blanks( "python")
