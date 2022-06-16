"""
create a loop that logs the numbers from -99 (ascending)"""

nums = range(0, 100, 1)

for n in nums:
    print(sorted(nums))
    break

"""
create a loop that logs the numbers from 99-0 (descending)"""


for n in nums:
    print(sorted(nums, reverse=True))
    break
    