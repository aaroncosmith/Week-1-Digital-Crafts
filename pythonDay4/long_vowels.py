# ask the user for a string
user_input = input("Please enter some words you'd like to give LOOOONG vowels to: ")

#make all characters the same
user_input = user_input.lower()

#begin the conversion
long_string = user_input.replace("a", "aaaaaa")
long_string = long_string.replace("e", "eeeeee")
long_string = long_string.replace("i", "iiiiiii")
long_string = long_string.replace("o", "ooooooo")
long_string = long_string.replace("u", "uuuuuuuu")

print(long_string)
