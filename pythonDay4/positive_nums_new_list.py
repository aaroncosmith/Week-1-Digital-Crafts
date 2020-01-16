nums = [2, -4, 8, -16, 32, -64]

#lets find the positive numbers out of this list and put it in a new list
positive_nums = []
for num in nums:
    if num > 0:
        positive_nums.append(num)
print(positive_nums)