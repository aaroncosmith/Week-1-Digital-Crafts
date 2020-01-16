# establish a string and make it uppercase
string = input("Welcome to the 1337 5P33K translator, enter your text here: ").upper()

# make some lists
letters_replace = "AEGIOST"
leet_speak = "4361057"
translation = ""

# use two for loops to make this happen
for index in range(len(string)):
    add_to = ""
    for inner_index in range(len(letters_replace)):
        if string[index] == letters_replace[inner_index]:
            add_to = str(leet_speak[inner_index])
            break
        else: 
            add_to = string[index]
    translation += add_to

print(translation)

