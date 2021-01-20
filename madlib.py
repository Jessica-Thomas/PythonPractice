# Madlib-- practicing input, output and variables

# Today I went to the zoo. I saw a(n) ___________(adjective) _____________(Noun) jumping up and down in its tree. 
# I got some peanuts and passed them through the cage to a gigantic gray _______(noun) towering above my head. 
# Feeding that animal made me hungry. I went to get a __________(adjective) scoop of ice cream. 
# It filled my stomach. Afterwards I had to __________(verb) __________ (adverb) to catch our bus. 
# When I got home I __________(verb, past tense) my mom for a __________(adjective) day at the zoo.

# prompt the user for parts of speech and store them in variables
adjective = input("Please enter an adjective:  ")
noun = input("Please enter a noun:  ")
noun2 =  input("Please enter a noun:  ")
adjective2 = input("Please enter an adjective:  ")
verb = input("Please enter a verb:  ")
adverb =  input("Please enter an adverb:  ")
verbpasttense = input("Please enter a past tense verb:  ")
adjective3 = input("Please enter an adjective:  ")

# output the template to the screen with the balnks filled in
print("Today I went to the zoo. I saw a(n)", adjective, noun, "jumping up and down in its tree. I got some peanuts and passed them through the cage to a gigantic gray", noun2, "towering above my head. Feeding that animal made me hungry. I went to get a", adjective2, "scoop of ice cream. It filled my stomach. Afterwards I had to", verb, adverb, "to catch our bus. When I got home I", verbpasttense, "my mom for a", adjective3, "day at the zoo.")

# print("Today I went to the zoo. I saw a(n) {} {} jumping up and down in its tree. I got some peanuts and passed them through the cage to a gigantic gray {}towering above my head. Feeding that animal made me hungry. I went to get a {}scoop of ice cream. It filled my stomach. Afterwards, I had to {} {} to catch our bus. When I got home I {} my mom for a {} day at the zoo.".format(adjective,noun,noun2,adjective2,verb,adverb,verb_past_tense,adjective3))

# BOOM. ^^Two ways to accomplish the same result. No errors.