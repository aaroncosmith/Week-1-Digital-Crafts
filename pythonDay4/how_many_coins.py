# prompt the user and ask if they want a coin
# coin_count = 0
# updated_coin_count = 0
# coin_msg= "You have " + str(updated_coin_count) + " coins. "
# do_want = input(coin_msg + "Do you want another?: ").lower()

# while do_want == "yes":
#     coin_count += 1
#     print(coin_msg)
#     print(do_want)
# else: 
#     print("Goodbye!")

# very incomplete, this is not working


# while updated_coin_count == coin_count:
#     if do_want == "yes":
#         updated_coin_count = updated_coin_count + 1
#         print(coin_msg)
#         continue
#         coin_count = coin_count + 1
#         continue
#         do_want

# WHYYYYYY I need to study my while loops more

# prompt user and ask if they want a coin
do_want_begin = input("You have 0 coins. Would you like another?: ").lower()
coin_count = 0


while do_want_begin == "yes":
    coin_count += 1
    coin_count_str = str(coin_count)
    print("You have " + coin_count_str + " coins. ")
    do_want = input("Would you like another?: ").lower()
    if do_want == "yes":
        continue
    else:
        print("Enjoy your coins!")
        break


#FINALLY



