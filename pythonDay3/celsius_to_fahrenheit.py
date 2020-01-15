# lets get the users input
c_temp = int(input("Temperature in C?: "))

# add our formula and send our change back

f_temp = c_temp * 1.8 + 32
f_temp_str = str(f_temp)
print("Your temperature is " + f_temp_str + "F")