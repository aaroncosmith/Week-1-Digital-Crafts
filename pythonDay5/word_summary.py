# lets make a word summary, it will count each time a word is used
# in a user given string!

user_string = input("Please paste something and i'll tell you how many times each word is used: ").lower()
the_dict = {}
#### split up the words from each other
#### MAYBE NOT HERE
#print(user_string.split())

# do the thing
for words in user_string.split():
    if words not in the_dict:
        the_dict[words] = 1
    else:
        the_dict[words] += 1

print(the_dict)

# lets sort it in amount of times it shows up
# i need to come back to this....
# sorted_d = sorted(the_dict.items(), key=lambda x: x[0])



