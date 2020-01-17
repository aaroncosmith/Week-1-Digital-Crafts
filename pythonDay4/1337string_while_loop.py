# establish a string and make it uppercase
string = input("Welcome to the 1337 5P33K translator, enter your text here: ").upper()

# make some lists
letters_replace = "AEGIOST"
leet_speak = "4361057"
translation = ""

# use two for loops to make this happen
for i in range(len(string)):
    # for each letter/index in the string
    add_to = ""
    for j in range(len(letters_replace)):
        #loop through all the letters_replace
        if string[i] == letters_replace[j]:
            add_to = str(leet_speak[j])
            break
        else: 
            add_to = string[i]
    translation += add_to

print(translation)

