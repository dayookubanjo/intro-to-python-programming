"""
Dictionaries are used to store data in key:value pairs

Key is like a column title while value is the actual value

e.g. Key = first_name and value = "Adedayo"
"""

#You must always put the key in " "

student = {"first_name": "John",
           "last_name": "Fashanu",
           "is_married": True ,
           "age": 34,
           "height": 6.5 ,
           "profession": ["Footballer" , "Musician"] ,
           "start_date": "2021-07-18" ,
           "location": (6.605874, 3.349149) ,
           }

print( type(student) ) # Data type is dictionary
print(student)
# Dictionaries are not indexed by numbers but by keys so you can't slice this way student[1]
# To display the value of a particular key
print( student["first_name"])
print( student["profession"])
# keys(): to display all keys in a dictionary
print( student.keys() )
# values(): to display all values in a dictionary
print( student.values() )
# Changing the value in a dictionary
student["first_name"] = "Emmanuel"
print(student)


"""
Be careful of making shallow copies in Python because any
changes to one will automatically apply to the other.
"""

student = {"first_name": "John",
           "last_name": "Fashanu",
           "is_married": True ,
           "age": 34,
           "height": 6.5 ,
           "profession": ["Footballer" , "Musician"] ,
           "start_date": "2021-07-18" ,
           "location": (6.605874, 3.349149) ,
           }

# Assuming student graduates & becomes an employee of the school
employee = student
print( employee )
print (employee["start_date"]) #start_date = 2021-07-18
print (student["start_date"]) #start_date = 2021-07-18
# Now let's update start_date in employee to reflect the employee's start date not school resumption date
employee["start_date"] = "2022-01-03"
# Notice below that both employee start date and student start date were updated which shouldn't be so.
print(employee["start_date"])
print(student["start_date"])


"""
TO AVOID THE ABOVE THE SHALLOW COPY ISSUE, USE DEEPCOPY TO CREATE A COPY
TO ENSURE THAT CHANGES TO ONE AREN'T REFLECTED IN THE OTHER
"""

student = {"first_name": "John",
           "last_name": "Fashanu",
           "is_married": True ,
           "age": 34,
           "height": 6.5 ,
           "profession": ["Footballer" , "Musician"] ,
           "start_date": "2021-07-18" ,
           "location": (6.605874, 3.349149) ,
           }

# Use the copy module in python to create a deepcopy
import copy
employee = copy.deepcopy( student )
print (employee["start_date"]) #start_date = 2021-07-18
print (student["start_date"]) #start_date = 2021-07-18
# Now let's update start_date in employee to reflect the employee's start date not school resumption date
employee["start_date"] = "2022-01-03"
# Notice below that this time only the employee start date was updated
print(employee["start_date"])
print(student["start_date"])


"""
List of dictionaries
"""

#List of students in a class
students = [
            {"first_name": "John",
           "last_name": "Fashanu",
           "is_married": True ,
           "age": 34,
           "height": 6.5 ,
           "profession": ["Footballer" , "Musician"] ,
           "start_date": "2021-07-18" ,
           "location": (6.605874, 3.349149) ,
           }
            ,

            {"first_name": "Obinna",
           "last_name": "Nwachukwu",
           "is_married": False ,
           "age": 28,
           "profession": "Business Owner" ,
           "start_date": "2021-07-12" ,
           }
    ]

"""
Notice in the above that we don't have the second student's
height & location and this wasn't a problem

This is similar to the concept used in some NOSQL databases
like Dynamodb where each item/object can have different
structures
"""

# Returns the first student in the list
print( students[0] )
# Returns the first name of the first student in the list
print( students[0]["first_name"] )
#update the profession of the second student from Business Owner to Banker
print( students[1]["profession"] ) # Business Owner
students[1]["profession"] = "Banker"
print( students[1]["profession"] ) # profession updated to Banker