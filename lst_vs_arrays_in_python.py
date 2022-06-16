"""lists and arrays are used to store data and they both allow indexing, slicing and iterating

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