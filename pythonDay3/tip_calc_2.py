# I copy/pasted from my last calculator

#start with user inputs

total_amount = float(input("Total bill amount?: $"))
service_level = str(input("Level of service? (good, fair, or bad): "))
split_ways = float(input("Amount of people splitting bill?: "))
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
total_split = total_with_tip / split_ways
#turn tip into a string
tip_amount = str(tip_amount)
total_with_tip = str(total_with_tip)
total_split = str(total_split)
# then display to user
print("Your tip amount is: $" + tip_amount)
print("Your total with tip is: $" + total_with_tip)
print("The amount per person is: $" + total_split)
# I think that's it 

#I need to add a converson for dollar amounts
#but ive had enough ;)