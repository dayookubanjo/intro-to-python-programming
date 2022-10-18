"""
A class is a template for creating objects

An object is an instance of a class. Its a real life entity

A class is like a table in a database with different
attributes/columns while object is like a record in the
table.

"""

#This allows you to create a class without any attributes
class Customer:
    pass

print( type(Customer) )

#create an instance of a Customer class
cust_1 = Customer()

# Creating attributes and Assigning values to the instance of a class.
cust_1.first_name = "Adedayo"
cust_1.last_name = "Okubanjo"
cust_1.age = 40

print( cust_1.first_name )

# Customer Instance 2
cust_2 = Customer()
#Create attributes & assign values
cust_2.first_name = "Layla"
cust_2.last_name = "James"
cust_2.age = 65

print(cust_2.age)


"""
To automate the process of assigning values to the instance
of a class, we use the init method.
"""

class Customer:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

cust_1 = Customer("Adedayo", "Okubanjo", 40)
cust_2 = Customer("Layla", "James", 65)
print ( cust_1.full_name )


#A class can also contain variables that act on the class data

#Say disposable income of our customers is 30% of their income

class Customer:
    def __init__(self, first_name, last_name, age, income):
        disposable_income_rate = 0.3
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name
        self.income = income
        self.disposable_income = income * disposable_income_rate

cust_1 = Customer("Adedayo", "Okubanjo", 40, 1200)
print ( cust_1.disposable_income )
cust_2 = Customer("Layla", "James", 65, 6500)
print ( cust_2.disposable_income )


"""
A method is a function in a class

Object methods are bound to the object.

Each object method in a class always takes
the instance as the first argument

Object methods have to be called by an object of the class

"""


class Customer:
    def __init__(self, first_name, last_name, age, income):
        disposable_income_rate = 0.3
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name
        self.income = income
        self.disposable_income = income * disposable_income_rate

    def ageindays(self):
        return self.age * 365

cust_1 = Customer("Adedayo", "Okubanjo", 40, 1200)
print( cust_1.ageindays() )
cust_2 = Customer("Layla", "James", 65, 6500)
print( cust_2.ageindays() )



"""
Static methods are bound to the class instead of the object

Static methods can be called without an object for the class

"""

class Customer:
    def __init__(self, first_name, last_name, age, income):
        disposable_income_rate = 0.3
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name
        self.income = income
        self.disposable_income = income * disposable_income_rate

    def ageindays(self):
        return self.age * 365

    def multiplyNumbers( a, b ):
        c = a * b
        return c

#I can call the method directly from the class
print( Customer.multiplyNumbers( 10, 15 ) )

# NOTE: Method ageindays() can only be called by an object of the class.
