"""lists and arrays are used to store data and they both allow indexing, slicing and 


to use an array in python you need to download the NumPy package or the array module

------------------------------------------
LISTS 
------------------------------------------
LISTS DO NOT NEED TO BE UNIQUE, ITEM DUPLICATION IS POSSIBLE, EACH ELEMENT HAS ITS OWN DISTINCT PLACE AND CAN BE ACCESSED SEPARATELY VIA THE INDEX

THE ELEMENTS INSIDE A LIST CAN BE OF DIFF DATA TYPES, YOU CAN HAVE STR, LISTS, TUPLES, INTS, DICTS, ETC INSIDE LISTS

------------------------------------------
ARRAYS
------------------------------------------
ARRAYS ARE ALSO ORDERED USUALLY UNABLE TO STORE NON-UNIQUE ITEMS BUT IT DEPENDS ON THE KIND OF ARRAY USED

- the python array module requires all array elements to be of the same type, to create an array you need to specify a value type

i.e:

array = arr.array("i", [1,2,3])

- the numpy array supports diff data types, to create a numpy array you only need to specify the items enclosed in square brackets

i.e:
array_2 = np.array(["numbers", 1,2,3,4])
------------------------------------------
so main difference?
------------------------------------------
1. arrays need to be declared and lists do not
2. arrays are more efficient in storing large amounts of data
3. arrays are great for numerical operations, lists cannot handle directly math operations. 
i.e.: you can divide each element of an array by the sam number with just one line of code but if you try and do that to a list you will get an error
------------------------------------------
you can still do math ops on a list but it is less efficient
------------------------------------------
    BOTTOM LINE: 
    
If you need to store a relatively short sequence of items and you don't plan to do any mathematical operations with it, a list is the preferred choice. This data structure will allow you to store an ordered, mutable, and indexed sequence of items without importing any additional modules or packages.
If you have a very long sequence of items, consider using an array. This structure offers more efficient data storage.
If you plan to do any numerical operations with your combination of items, use an array. Data analytics and data science rely heavily on (mostly NumPy) arrays.
"""

""" 1- Define an empty list named foods 
"""
foods = []
# print(type(foods))

"""2 - Add the strings 'pizza' & 'cheeseburger' & 'taco' to the foods list"""

foods.append('cheeseburger')
foods.append('pizza')
foods.append('taco')
# print(foods)

"""3 Access the string 'pizza' (based upon its known position)
"""
# print(foods[1])

for i in foods:
    # print(foods[1])
    break

"""4 Insert the string 'tofu' in the foods array between 'pizza' and 'taco'"""

"""
---------------------------------------------------------------------------------------------------------------------------------------------
in python the insert method allows you to insert an element to a list at the specified index 
---------------------------------------------------------------------------------------------------------------------------------------------

i.e.)

list_name.insert(index, item_inserting)

"""
for i in foods:
    foods.insert(2, 'tofu')
    # print(foods)
    break




"""5 replace the string 'aple' in the array with the string 'chicken nuggets' using index"""

a_list = ['aple', 'orange', 'aple', 'banana', 'grape', 'aple']

a_list[0] ='chicken nuggets'
a_list[2] = 'chicken nuggets'

b_list = a_list
# print(b_list)



"""Replace a particular item in a Python list with a for loop"""
a_list = ['aple', 'orange', 'aple', 'banana', 'grape', 'aple']
# print(a_list)
for i in range(len(a_list)):
    if a_list[i] == 'aple':
        a_list[i] = 'apple'
# print(a_list)



"""using list comprehensions"""

"""Replace a particular item in a Python list using a list comprehension"""
a_list = ['aple', 'orange', 'aple', 'banana', 'grape', 'aple']
# print(a_list)
a_list = ['apple' if item == 'aple' else item for item in a_list]
# print(a_list)


"""change all values in a list using a function
"""
a_list = ['aple', 'orange', 'aple', 'banana', 'grape', 'aple']

def replace_all(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]

replaced_list = replace_all(a_list, 'aple', 'apple')
# print(replaced_list)


a_list = ['aple', 'ornge', 'aple', 'banana', 'grape', 'aple']
for i in range(len(a_list)):
    if a_list[i] in ['aple', 'ornge']:
        a_list[i] = 'typo'
# print(a_list)


a_list = ['aple', 'ornge', 'aple', 'banana', 'grape', 'aple']
for i in range(len(a_list)):
    if a_list[i] == 'aple':
        a_list[i] = 'apple'
    elif a_list[i] == 'ornge':
        a_list[i] = 'orange'
print(a_list)