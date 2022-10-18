"""
A module is simply a python file that contains a set of
related functions, classes or variables that have been defined
and can be reused across your application by importing
"""


"""

Create two modules (python files).

Ensure they are in the same folder as this file we are working on

Module 1: arithmetic.py

def add(a,b):
    c = a + b
    return c

def divide(a,b):
    c = a / b
    return c

pi = 3.14159

Module 2: sales.py

def vatamount(saleamount, vatpercent):
    b = saleamount * vatpercent
    return b

def netrevenue(grossrevenue, discounts):
    b = grossrevenue - discounts
    return b

"""

#From arithmetic module import fxn add() & var pi

from arithmetic import add
from arithmetic import pi

print( add(pi , 10) )


#From sales module import fxn netrevenue() & var pi

from sales import netrevenue

#grossrevenue=1000 & discount=200
print( netrevenue(1000, 200) )



"""
A package is a directory that contains multiple modules
and a __init__.py file
"""

#From package mypackage import module sales
from mypackage import sales

# Now i have to reference the function using sales. because I have imported the full module

print( sales.netrevenue(1000, 200) )
