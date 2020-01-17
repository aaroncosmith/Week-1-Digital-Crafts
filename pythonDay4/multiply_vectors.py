x = [2, 4, 8, 16, 32, 64]
y = [1, 3, 7, 15, 31, 63]
z = []
# we have two lists and we want to create a new list by multiplying
# the pairs of numbers in corresponding positions in the two lists.

#z.append(x[0]* y[0])
#z.append(x[1]* y[1])
#z.append(x[2]* y[2])
#z.append(x[3]* y[3])
#z.append(x[4]* y[4])
#z.append(x[5]* y[5])

#print(z)

# that's a lame way of doing it

#while len(z) < 6:
#    for each_x in x:
#        z.append(each_x)
#    for each_y in y:
#        for each_z in z:
#            each_x * each_y

#okay that's way easier...

for each_index in range(len(x)):
    z.append(x[each_index] * y[each_index])


print(z)


