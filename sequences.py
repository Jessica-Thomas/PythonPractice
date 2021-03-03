groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

# index = 1
# for item in groceries:
#     print(item)



# f-string

# for item in groceries:
#     print(f'{index}. {item}')
#     index+=1


# enumerated object
for index, item in enumerate(groceries):
    print(f'{index}. {item}')
    # starts at 0 bc 0 index

for index, item in enumerate(groceries, 1):
    print(f'{index}. {item}')
    # pass second argument to get list to start at 1