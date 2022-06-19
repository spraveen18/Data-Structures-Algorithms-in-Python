# Write a function called "show_excitement" where the string
# "enter any string!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.


def show_excitement():
    return ' '.join(['enter any string!'] * 5)

print show_excitement()


# def show_excitement():
#     # Your code goes here!
#     value = str(input("enter a string: "))
#     value_str = value*5
#     return ' '.join(value_str)

# print(show_excitement())
