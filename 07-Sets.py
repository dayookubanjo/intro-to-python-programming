"""
- A set is a container that holds a unique set of values.
- Sets are used to remove duplicates in a list of values.
- Sets are are unindexed and unordered.
- They are created using {} or set() constructor.
"""

#Notice below that Nike is stated twice
brand_set = {"Nike","Gucci","Fendi","EkiOris","Tom Ford","Nike" }
print( type(brand_set) )
#Sets automatically removes duplicates (Nike in this case)
print( brand_set )


student_age = {32, 28, 25, 34, 25, 18, 21, 22, 32, 39, 42}
#Returns a unique set of age that exists in the set
print( student_age ) #32 & 25 returned once


"""
Sets are unindexed

You will get an error if you try to run the below query:

brand_set = {"Nike","Gucci","Fendi","EkiOris","Tom Ford","Nike" }
print( brand_set[0] )
"""

brand_set = {"Nike","Gucci","Fendi","EkiOris","Tom Ford","Nike" }
# Check if an item exists in a set
print("Guess" in brand_set)
# returns True if the item exists in a set and False if it doesn't
print("Fendi" in brand_set)


"""
Set Methods
"""

teacher_age = {54, 33, 32, 28, 61, 48, 39, 32, 37, 55}
student_age = {32, 28, 25, 34, 25, 18, 21, 22, 32, 39, 42}
# Union: Returns a unique set of values in the two sets
print ( student_age.union(teacher_age) )
# Intersection: Returns a set of values that exists in the two sets
print ( student_age.intersection(teacher_age) )
# Difference: Returns a set of values that are unique to each set
print ( student_age.difference(teacher_age) )


brand_set = {"Nike","Gucci","Fendi","EkiOris","Tom Ford" }
print(brand_set)
# add(): Used to add a new item to a set
brand_set.add("Lacoste")
print(brand_set)
# remove(): remove an item from a set
brand_set.remove("Tom Ford")
print(brand_set)
# clear(): used to empty a set
brand_set.clear()
print(brand_set)
#Delete a set
del brand_set
