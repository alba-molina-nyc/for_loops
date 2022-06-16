"""
1.create a loop that logs the numbers from -99 (ascending)"""

nums = range(0, 100, 1)

for n in nums:
    # print(sorted(nums))
    break

"""
2.create a loop that logs the numbers from 99-0 (descending)"""

for n in nums:
    # print(sorted(nums, reverse=True))
    break

"""
try with less code: 
"""

for i in range(0,100,1):
    #  print(sorted(range(0,100,1)), 'ascending')
    #  print(sorted(range(0,100,1), reverse=True), 'descending')
     break

"""3. Create a loop that logs the EVEN numbers from 0-98 (ascending)"""

for i in range(0,100,1):
    if i % 2 == 0:
        # print(i, 'evens')
        break
  

"""4. Create a loop that logs the EVEN numbers from 98-0 (descending)"""

for i in range(0,100,1):
    if i % 2 == 0:
        # print(sorted(range(0,100,1), reverse=True))
        break


"""5. Create a loop that logs the ODD numbers from 0-99 (ascending)"""

for i in range(0,100,1):
    if i % 2 != 0:
        # print(i)
        break

"""6. Create a loop that logs the ODD numbers from 99-0 (descending)"""
for i in range(0,100,1):
    if i % 2 != 0:
        # print(sorted(range(0,100,1), reverse=True))
        break

"""7. Create a loop that logs the numbers from 49-72 (ascending)"""
for i in range(49,73,1):
    # print(i)
    break

"""using slicing"""

numbs = range(0,100,1)

for n in numbs:
    print(sorted(numbs[49:]))
    break

"""8. Create a loop that logs the numbers from 81-26 (descending)"""

"""9. Create a loop that logs the numbers from 3-90 that are multiples of 3 (ascending)"""