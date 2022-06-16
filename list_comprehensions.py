"""
list comprehensions: will run faster && this could matter for larger data sets
this page will do the for loops in prior doc and attempt with list comprehensions
"""
"""
1.create a loop that logs the numbers from 0 -99 (ascending)"""
# first_task = [i for i in whatever if i == 0] etc

first_task = [i for i in range(0,100,1) if i >= 0]
# print(first_task, 'listcomp')

"""
2.create a loop that logs the numbers from 99-0 (descending)"""

second = [i for i in range(0,100,1) if i >= 0]
# print(second)


"""
3. Create a loop that logs the EVEN numbers from 0-98 (ascending)"""

evens_third = [i for i in range(0,99,1) if i % 2 == 0]
# print(evens_third)

"""4. Create a loop that logs the EVEN numbers from 98-0 (descending)"""

evens_descending = [i for i in range(0,99,1) if i % 2 == 0]
# print(sorted(evens_descending, reverse=True))

"""5. Create a loop that logs the ODD numbers from 0-99 (ascending)"""

odds_ascending = [i for i in range(0,100,1) if i % 2 == 1]
# print(sorted(odds_ascending, reverse=False))


"""6. Create a loop that logs the ODD numbers from 99-0 (descending)"""

odds_descending = [i for i in range(0,100,1) if i % 2 == 1]
# print(sorted(odds_ascending, reverse=True))

"""7. Create a loop that logs the numbers from 49-72 (ascending)"""

asc_slice = [i for i in range(49,73,1)[:49] if i]
# print(asc_slice)

"""8. Create a loop that logs the numbers from 81-26 (descending)"""

desc_slice = [i for i in range(26,82,1)[:26] if i]
print(sorted(desc_slice, reverse=True))


"""9. Create a loop that logs the numbers from 3-90 that are multiples of 3 (ascending)"""
multiples_3 = [i for i in range(3,90) if i % 3 == 0 ]
print(multiples_3)



