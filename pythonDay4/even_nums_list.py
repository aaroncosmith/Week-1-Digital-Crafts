nums = [2, 4, 8, 16, 32, 64, 21]

# find the even numbers in this list
# lets to a for loop to check each number
# then make sure it has no remainder when % 2

for num in nums:
    if num % 2 == 0:
        print(num)
