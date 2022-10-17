"""
- A tuple is a container that can hold multiple values.
- Unlike lists, tuples are immutable/unchangeable just like strings.
- They allow duplicate members.
- It is created using () or tuple() constructor.
- You use a tuple when you dont want the content to ever be altered
e.g. (latitude, longitude) , Credit Card Info.
"""

# You don't expect the lat & lon of a location to change

accra = (5.614818, -0.205874)
print(accra)
print( type(accra) )

"""
Slicing a tuple
"""

"""
Because tuples are immutable, you will get an error
if you try to change the value in a tuple.

toronto=(43.653908, -79.384293)
toronto[1] = 4.657498
"""


"""
If you have a tuple with only one value, make sure to
add a trailing comma when creating it
"""

toronto_latitude = (43.653908)
print( type(toronto_latitude) )
toronto_latitude = (43.653908, )
print( type(toronto_latitude) )


# len(): used to get the number of objects in a tuple
toronto=(43.653908, -79.384293)
print( len(toronto) )
# del: used to delete a tuple
del toronto
# print(toronto)
