power_rangers = ["Jason", "Trini", "Zack", "Billy", "Kim", "Tommy"]

#ask user to remove someone in the list
who_to_remove = input("Who would you like to remove?: ")


if who_to_remove in power_rangers:
    power_rangers.remove(who_to_remove)
    print(power_rangers)
else:
    print("%s is gone." % (who_to_remove))

#STUDY YOUR STRING CONCATENATION!! and learn how to spell