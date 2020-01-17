# establish a string
string = "This is the string im going to change into what I want. Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following charact"
#make it lowercase
# string = string.lower()
#change into characters
# string1337 = string.replace("a", "4")
# string1337 = string1337.replace("e", "3")
# string1337 = string1337.replace("g", "6")
# string1337 = string1337.replace("i", "1")
# string1337 = string1337.replace("o", "0")
# string1337 = string1337.replace("s", "5")
# string1337 = string1337.replace("t", "7")

#assingment said to make upper so ill do that now
# string1337 = string1337.upper()

leet_translator = {
    "a": "4",
    "e": "3",
    "g": "6",
    "i": "1",
    "o": "0",
    "s": "5",
    "t": "7",
}

result = "";

for eaIndex in range(len(string)):
    print(str(leet_translator[string[eaIndex]]))


print(string1337)



