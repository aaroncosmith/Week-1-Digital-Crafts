# ask the user for a string
user_input = input("Please enter some words you'd like to give LOOOONG vowels to: ")

#make all characters the same
user_input = user_input.lower()

#begin the conversion
long_string = user_input.replace("aa", "aaaaaa")
long_string = long_string.replace("ee", "eeeeee")
long_string = long_string.replace("ii", "iiiiiii")
long_string = long_string.replace("oo", "ooooooo")
long_string = long_string.replace("uu", "uuuuuuuu")

print(long_string)
