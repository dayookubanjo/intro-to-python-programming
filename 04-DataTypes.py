"""
1) STRINGS
"""

"""
Strings are characters or texts represented using "", '' or """ """ for multiline str.
"""

first_name = "Adedayo"
print(first_name)
# Check the data type of the variable first_name
print( type(first_name) )

last_name = 'Okubanjo'
print(last_name)
# Check the data type of the variable last_name
print( type(last_name) )

full_name = "Adedayo Okubanjo"
print(full_name)

occupation = "Data Scientist"
print(occupation)


Age = "72"
print(Age)
"""
You will notice below that the data type of Age variable is String.
This is because we wrapped the 72 inside a string literal "" hence it's converted to a string.
"""
print( type(Age) )

NewAge = 72
print(NewAge)
"""
You will notice below that the data type of NewAge variable is Integer because
we are no longer wrapping the 72 inside a string literal.
"""
print( type(NewAge) )


"""
STRING CONCATENATION
"""

first_name = "Adedayo"
# + is used for concatenating strings
print("My name is" + first_name)
# Make the sentence clearer by adding some space in between "My name is" and first_name variable
print("My name is" + " " + first_name)
# Add a full stop at the end of your sentence
print("my name is" + " " + first_name + ".")


# You can also concatenate with " , " instead of " + "
first_name = "Adedayo"
print("My name is",first_name)
"""
You will notice that the output of the above automatically adds space before the first_name
which does not require us to add an extra space " ".
"""


# Example 2

print("Adedayo is a data scientist and works with TD bank")
print("I have always wanted to be a data scientist")
print("TD bank is a wonderful organization to work with")
print("Adedayo loves Python programming")

#Let us try to simplify this by using variables

first_name = "Adedayo"
profession = "Data Scientist"
place_of_work = "TD Bank"
# Now print the statements using the variables above
print(first_name + " is a " + profession + " and works with " + place_of_work )
print("I have always wanted to be a " + profession)
print(place_of_work + " is a wonderful organization to work with")
print(first_name + " loves Python programming")


# You can now reprint the statements for new users by just changing the values of the variables

first_name = "Alianna"
profession = "Software Engineer"
place_of_work = "Rogers"
# Now print the statements using the variables above
print(first_name + " is a " + profession + " and works with " + place_of_work )
print("I have always wanted to be a " + profession)
print(place_of_work + " is a wonderful organization to work with")
print(first_name + " loves Python programming")

"""
NOTE THAT YOU CAN ONLY CONCATENATE STRINGS

For example, If you try to concatenate a string with an integer, you will get an error.

age = 35
print("My age is " + age)
"""

#You have to convert an integer to string before concatenating using str() or using quotation marks

age = "35"
print("My age is " + age )

#OR

age = 35
print( "My age is " + str(age) )


"""
FORMAT & F-STRING
"""

# They are used to pass values into a string without the need for concatenation

"""
a) FORMAT
"""

print( "My name is {}, and i am {} years old.".format("Adedayo", 72) )

# You can use format and f string to also pass values in a variable to a string

first_name = "Adedayo"
age = 72
print( "My name is {}, and i am {} years old.".format(first_name, age) )

"""
a) F-STRING
"""

first_name = "Adedayo"
age = 72
print( f"My name is {first_name}, and i am {age} years old.")

occupation = "Tailor"
print( f"I am a {occupation}." )

"""
SLICING STRINGS
"""

# Note: Python counts from 0 not 1

test = "This Is A String In Python"
print( test[0] )
print( test[0:6] ) #Note that the last number specified is always excluded
print( test[3:10] )
print( test[:7] ) #If you don't specify start index, it equals to 0
print( test[0:7] )
print( test[-1] ) #First Index from the back = Last Index
print( test[-2] ) #Second Index from the back
print( test[0:-1] ) #0 to -2 (ignore the last index)


"""
STRING METHODS
"""

province = "ontaRIO"
print( province )
# Capitalizes a string (First letter becomes upper case, others lower case)
print( province.capitalize() )
# upper: Converts a string to all upper case
print( province.upper() )
# lower: Converts a string to all lower case
print( province.lower() )
# len: returns the lenght of string
print( len(province) )

# replace: replaces string
province = "ontaRIO"
print( province.replace('RIO','rio province') )

city = "vancouver"
# counts the occurence of 'a' in city variable
print( city.count('a') )
# returns True if city starts with 'a' otherwise it returns False
print( city.startswith('a') )
# returns True if city ends with 'r' otherwise it returns False
print( city.endswith('r') )


#Split

#Splits a value into a list using a separator: default separator is space

fullname = "Adedayo Okubanjo"
# splits fullname into a list using space as default seperator
print( fullname.split() )

# You can specifiy a separator character as well
NewFullname = "Adedayo-Okubanjo"
print( NewFullname.split("-") )


#Find: Returns the index position of the value passed

fullname = "Adedayo Okubanjo"
# returns the index position of the first 'o' in fullname returns -1 if absent
print(fullname.find('o'))


"""
isalnum: returns True if variable is alphanumeric and
False if variable contains space or contains special characters

"""

var1 = "2face"
var2 = "737"
var4 = "Python is the best"
var5 = "sd-/!"
var6 = "!-/>"
print( var1.isalnum() )
print( var2.isalnum() )
print( var4.isalnum() )
print( var5.isalnum() )
print( var6.isalnum() )


"""
isalpha: returns True if a variable is all alphabets
and False if not all alphabets
"""

var3 = "Wizkid"
var2 = "737"
print( var3.isalpha() )
print( var2.isalpha() )


"""
isnumeric: eturns True if a variable is all numbers
and False if not all numbers
"""

var3 = "Wizkid"
var2 = "737"
print( var3.isnumeric() )
print( var2.isnumeric() )


"""
Strings are immutable: This means that you cannot change the string object itself
but you can change the reference variable using its method.
"""

name = "Dayo"
# Let's assume that my name is Bayo not Dayo so i need to change the D to B.
#You can't modify the string object itself
name[0] = "B"

#You can change the reference variable using it's method
name = "Dayo"
name = name.replace("D", "B")
print( name )


"""
2) NUMBERS
"""

# Numbers can either be whole numbers (integers) or numbers with decimal places (float)

age = 37
print( type(age) ) # Integer

temperature = 29.5
print ( type(temperature) ) # Float

#Use int() method to convert a string of numbers to integer

age = "75"
print( type(age) ) # String
# Convert age from string to integer using the int() method
age = int(age)
print( type(age) ) # String

# Use float() method to convert a string of numbers or integer to float

age = 45
print( type(age) ) # Integer
# Convert age from integer to float using the float() method
age = float(age)
print( age ) # This will now be 45.0 instead of 45
print( type(age) ) # Float


temperature = "28.5"
print( type(temperature) ) # String
# Convert temperature from string to float using the float() method
temperature = float(temperature)
print( type(temperature) ) # Float

"""
These type conversions are very important for
when you want to perform arithmetic operations.
"""

age = "40"
son_age = 12
# What is the difference btw my age and that of my son
"""
The operation below will throw an error because age="40" is a string
and you can't carry out arithmetic operations on strings

age_diff = age - son_age
"""
# Convert age to integer first before calculating the age difference
age = int(age)
age_diff = age - son_age
print(age_diff)
