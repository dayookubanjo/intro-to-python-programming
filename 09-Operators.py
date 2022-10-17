original_price = 1000
selling_price = 750
# 1) Subtraction (-)
discount = original_price - selling_price
print( discount )
# Same as just saying
print ( 1000 - 750 )
# 2) Addition (+)
print( selling_price + discount )
print ( 750 + 250 )


# 3) Multiplication (*)
selling_price = 750
vat_rate = 0.075
vat_amount = selling_price * vat_rate
print(vat_amount)
# Same as:
print ( 750 * 0.075 )
# 4) Division (/)
print( vat_amount / selling_price )
# 5) Raise to power
print( vat_amount ** 3)


"""
6) Equal to:

= Used to assign values to a variable
== Used to compare two variables
"""

a = 3
b = 5
print ( a )
print ( b )
print ( a == b ) #returns True if condition is true otherwise False


"""
Other Operators:

- Greater than: >
- Less than: <
- Greater than or equal to: >=
- Less than or equal to: <=
- Not equal to: <>

"""


"""
AND operator:

AND compares two conditions and
returns True if both conditions are true, otherwise False

"""

age = 23
print ( age >=13 and age <= 19 )

"""
OR operator:

OR compares two conditions and returns True if either of both
conditions are met, otherwise False

"""

income = 30
location = "Toronto"

print ( income >= 100 or location == "Accra" )
print ( income >= 20 or location == "Accra" )
