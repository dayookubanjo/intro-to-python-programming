"""
A variable is a reserved memory location for storing values for easy reference
in the future.

Variables can be of different types e.g. string, integers, decimal, boolean.

You can name your variables anything they must just follow certain rules:

Rules for Python variables:

A variable name must start with a letter or the underscore character.
A variable name cannot start with a number.
A variable name can only contain alpha-numeric characters and underscores
(A-z, 0-9, and _ ).
Variable names are case-sensitive (age, Age and AGE are three different variables).
"""

name = "Dayo"
# Print the content of name variable
print (name)
# Print the data type of name variable
print ( type(name) ) # Should be a string

age = 72
# Print the content of age variable
print (age)
# Print the data type of age variable
print ( type(age) ) # Should be an Integer

ismarried = True
# Print the content of ismarried variable
print (ismarried)
# Print the data type of ismarried variable
print ( type(ismarried) ) # Should be a boolean

isstudent = False
# Print the content of isstudent variable
print (isstudent)
# Print the data type of isstudent variable
print ( type(isstudent) ) # Should be a boolean


# We can use a variable in a sentence
name = "Adedayo"
print( "My name is" + " " + name + "." )
