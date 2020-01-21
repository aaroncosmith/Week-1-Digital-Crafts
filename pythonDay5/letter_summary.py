# make a letter_histogram program that asks for user input, then prints a
# dictionary containing the tally of how many times each letter was used.


# for letters in string:
#     if letters not in the_dict:
#         the_dict[letters] = 1
#     else:
#         the_dict[letters] += 1

# print(the_dict)

# I could only figure this out with the not in thing... it works but there's
# got to be a better way to do this...

# well lets clean it up

user_input = input("Write something and I will count how many times each letter was used: ").lower()
the_dict = {}

for letters in user_input:
    if letters not in the_dict:
        the_dict[letters] = 1
    else:
        the_dict[letters] += 1

# good bye space # i could probably make this an elif statement above, but whatever :)
if " " in the_dict:
    del the_dict[" "]

# sort the dict
for key in sorted(the_dict.keys()):
    print(key, " :: ", the_dict[key])

# boom! 



