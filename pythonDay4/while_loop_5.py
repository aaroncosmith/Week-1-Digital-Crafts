postive = "I hope your having a really great day!"

#STOP = 10
count = 0

while count < len(postive):
    if (count % 2) == 0 and postive[count] != ' ':
        print(postive[count])
    count += 1
