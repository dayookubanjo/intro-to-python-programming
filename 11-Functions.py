"""
Functions are used to bundle a set of instructions that you
want to use repeatedly.

They are usually written to carry out a specific task

Be mindful with Indentation

Syntax:

def function_name():
    task
    return output

Function Call:

function_name()

"""

def printfxn():
    return "This is a test function."

print ( printfxn() )


# function with a parameter

# Square Function
def squarefxn (a):
    b = a ** 2
    return b

print ( squarefxn(10) )
print ( squarefxn(25) )
print ( squarefxn(173) )


#add function
def add(a,b):
    c = a + b
    return c

print ( add(10,15) )
print ( add(75,83) )
print ( add(135,39) )


#You can add as many parameters as needed to your function
def multiply (a,b,c):
    d = a * b * c
    return d

print( multiply(15,45,76) )
print( multiply(93,53,1045) )
