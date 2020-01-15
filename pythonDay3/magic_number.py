#prompt the user for a number
#compare that number to a predefined number
# if # match, tell user they are a mind reader
# if # not match, tell them to try again

user_input = int(input("What number (1- 10) am I thinking of? "))

MAGICNUMBER = 7

if user_input == MAGICNUMBER:
    print("You are a mind-reader!!!?!?!")
else: 
    print("HAHA try again!!")

