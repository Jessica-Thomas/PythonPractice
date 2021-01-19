input_name = input('What is your name?  ')

if input_name == "Tony":
    print("Fuck you, " + input_name)
elif input_name == "Ezekial":
    print("Fuck you, " + input_name)
else:
    print("Hello, ",input_name)
    
    age = int(input("How old are you?  "))
    if age >= 27:
        print('Way to be old.')

    print("I am glad you are not Ezekial or Tony.")
    print("Have a great day, {}!".format(input_name))