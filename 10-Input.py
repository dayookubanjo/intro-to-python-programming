"""
Input function allows users to insert a value into a program.

Every value entered into an input by the user is a string by default.
"""

nationality = input("Enter Nationality: ")
print ( f"I am {nationality}." ) # F-String
# Same as:
print ( "I am " + nationality + ".") # Concatenation


# Let's build a simple addition program

first_number = int ( input("Enter the first number: ") )
second_number = int( input("Enter the second number: ") )
add_result = first_number + second_number
print( f"The sum of the two numbers is: {add_result}." )
