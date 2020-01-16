nums = [2, 4, 8, 16, 32, 64]
FACTOR = 4
# time to multiply the numbers in the list against a factor
times_five = []
for num in nums:
    times_five.append(num * FACTOR)
print(times_five)
