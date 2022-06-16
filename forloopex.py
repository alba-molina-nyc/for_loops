"""
create a loop that logs the numbers from -99 (ascending)"""

from pydoc import describe


nums = range(0, 100, 1)

for n in nums:
    # print(sorted(nums))
    break

"""
create a loop that logs the numbers from 99-0 (descending)"""


for n in nums:
    # print(sorted(nums, reverse=True))
    break


"""
try with less code: 
"""

for i in range(0,100,1):
     print(sorted(range(0,100,1)), 'ascending')
     print(sorted(range(0,100,1), reverse=True), 'descending')
     break

