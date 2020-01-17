# prompt the user and ask if they want a coin

do_want = input("Do you want another?: ").lower()
coin_count = 0
coin_msg= "You have " + str(coin_count) + "coins. "

while do_want == "yes":
    coin_count += 1
    print(coin_msg)
    do_want
else: 
    print("Goodbye!")

# very incomplete, this is not working yet