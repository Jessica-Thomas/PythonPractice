# print("A")
# try:
#     result = "test" + 5
#     print("B")
# except ValueError:
#     print("C")
# except TypeError:
#     print("D")
# else:
#     print("E")
# print("F")


# print("A")
# try:
#     result = 5 + 5
#     print("B")
# except ValueError:
#     print("C")
# except TypeError:
#     print("D")
# else:
#     print("E")
# print("F")

def suggest(product_idea):
    if len(product_idea) < 3:
        raise ValueError("Idea should be more than 3 charaters")
    
    return product_idea + "inator"


    