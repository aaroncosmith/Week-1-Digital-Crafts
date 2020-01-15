#prompt user for two things, total bill amount and the level of service- good, fair, or bad

#calc tip amount and the total amount
#(bill amount + tip amount)
#good -> 20%
#fair -> 15%
#bad -> 10%


#start with user inputs

total_amount = float(input("Total bill amount?: $"))
service_level = str(input("Level of service? (good, fair, or bad): "))
tip_amount = 0

# do some functions
if service_level == "good":
    tip_amount = total_amount * .20
elif service_level == "fair":
    tip_amount = total_amount * .15
elif service_level == "bad":
    tip_amount = total_amount * .10
else:
    print("Please choose either good, fair, or bad, thanks!")

total_with_tip = total_amount + tip_amount

#turn tip into a string
tip_amount = str(tip_amount)
total_with_tip = str(total_with_tip)

# then display to user
print("Your tip amount is: $" + tip_amount)
print("Your total with tip is: $" + total_with_tip)

# I think that's it 
#I need to add a converson for dollar amounts
#but ive had enough ;)