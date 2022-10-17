"""
There are other data types used to store collection of data such as List, Tuple, Set & Dictionary.

In this section, we will be focusing on LISTs:
A list is a variable/collection that can hold multiple values of different data types.

- It is one of the most commonly used data types.
- Unlike strings, lists are mutable/changeable.
- They allow duplicate members.
- It is created using [] or list constructor. MOST COMMONLY USED APPROACH IS []
"""

list1 = ["Adedayo", "Okubanjo", 35, 5.11, True ]
# Check that the data type is List
print( type(list1) )
print(list1)

#Second Approach using list() constructor

list2 = list( ("Adedayo", "Okubanjo", 35, 5.11, True) )
# Check that the data type is List
print( type(list2) )
print(list2)

# A list of student age
student_age = [32, 22, 28, 45, 18, 36]
print(student_age)

# A list of cars
cars = ["Toyota", "Honda", "Kia", "Mercedes", "Nissan"]
print(cars)

"""
Exercise:
- Create a list of your favorite food.
- Create a list of your friends names.
- Create a list of your family member's year of birth.
"""


"""
List Slicing
"""
student_age = [32, 22, 28, 45, 18, 36]
print ( student_age[0] ) #Python starts counting from 0
print ( student_age[1] )
print ( student_age[0:3] ) #Last index 3 is ignored
#Same as above, starts from 0 where start index not specified
print ( student_age[:3] )
print ( student_age[3:6] )
print ( student_age[-1] ) #Last item in the list
print ( student_age[-2] ) #Second to last item in the list


"""
List Slicing
"""
cars = ["Toyota", "Honda", "Kia", "Mercedes", "Nissan"]
#Assuming i want to update "Nissan" in car_list to "Hyundai"
print(cars) # Before update
cars[4] = "Hyundai"
print(cars) # After update


"""
List Methods
"""
cars = ["Toyota", "Honda", "Kia", "Mercedes", "Nissan"]
print(cars)
# len(): returns the number of items in a list
print( len(cars) )
# append(): used to add a new item to a list
# Let's add a new car brand to the car_list
cars.append("Lexus")
print(cars)
# extend(): used to add more than one item to a list
cars.extend( ["Acura", "Range Rover", "Skoda"] )
print(cars)
# insert(): used to add a new item to a particular position
cars.insert(3, "Bentley")
print(cars)
# remove(): used to remove a particular item from a list
cars.remove("Lexus")
print(cars)
# pop(): used to remove a particular item from a list using the index
cars.pop(2)
print(cars)


# reverse(): used to rearrange a list from the last item to the first item
student_age = [32, 22, 28, 45, 18, 36]
student_age.reverse()
print( student_age )


# sort(): used to sort a list in ascending order or descending order
student_age = [32, 22, 28, 45, 18, 36]
print(student_age)
#ascending order
student_age.sort()
print( student_age )
#descending order
student_age.sort(reverse=True)
print( student_age )


"""
Splitting a list into variables
"""
student = ["Adedayo", "Okubanjo", 35, 5.11, True ]
print( student )
first_name, last_name, age, height, ismarried = student
print( first_name )
print( last_name )
print( age )
print( height )
print( ismarried )


"""
List aggregation
"""

student_age = [32, 22, 28, 45, 18, 36]
# Sums all elements of a list where all list elements are numeric(integers or float)
print( sum(student_age) )

#Import statistics package to access aggregation functions such as mean and median
import statistics as st
student_age = [32, 22, 28, 45, 18, 36]
#Returns average of the list
print ( st.mean(student_age) )
#Returns median of the list

print ( st.median(student_age) )
#Returns maximum number in the list

print ( max(student_age) )
#Returns minimum number in the list
print ( min(student_age) )
