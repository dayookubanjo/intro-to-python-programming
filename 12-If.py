"""
if statements are used to evaluate whether an expression is true
and perform an operation if true.

Be mindful with Indentation

Syntax:

if condition:
    operation

"""

divisor = 0

if divisor == 0:
    print("This number is zero and cannot be used as a divisor")


divisor = 3

if divisor == 0:
    print("This number is zero and cannot be used as a divisor")


order_amount = 100

if order_amount < 1000:
    print("Minimum order value is 1000 USD.")


"""
If Else
"""

# Else statement is used to perform an alternative operation if the expression is false

order_amount = 2000

if order_amount < 1000:
    print("Minimum order value is 1000 USD")
else:
    vat_amount = order_amount * 0.075
    print(f"Your vat amount in USD is: {vat_amount}.")


order_amount = 800

if order_amount < 1000:
    print("Minimum order value is 1000 USD")
else:
    vat_amount = order_amount * 0.075
    print(f"Your vat amount in USD is: {vat_amount}.")


"""
We can put this logic in a function to calculate our vat amount
whenever there's an order on our website.
"""

def vat_amount_fxn(order_amount):
    if order_amount < 1000:
        return "Error: Minimum order value is 1000 USD"
    else:
        vat_amount = order_amount * 0.075
        return f"Your VAT Amount is: {vat_amount}."

print( vat_amount_fxn(20000) )
print( vat_amount_fxn(400) )


"""
Else If
"""

# Else if (elif) is used to check for multiple expressions

"""
E.g.

Let's assume that a company running a marketing campaign need to
carry out the below checks to determine the type of ad to be
shown to prospect.

Check what age group a prospect falls under and show ad for
that age group.

Check that prospect falls within target market (18 - 55).

"""

age = 24

if age >= 13 and age <= 19:
   print ("Prospect is a teenager.")
elif age >= 20 and age <= 35:
   print ("Prospect is a young adult.")
elif age >= 36 and age <= 55:
   print ("Prospect is middle aged.")
else:
   print ("Prospect is out of our target market.")


# Let's put it in a function so we can call it with dynamic values multiple times

def determineProspectAgeBracket(age):
    if age >= 13 and age <= 19:
        print ("Prospect is a teenager.")
    elif age >= 20 and age <= 35:
        print ("Prospect is a young adult.")
    elif age >= 36 and age <= 55:
        print ("Prospect is middle aged.")
    else:
        print ("Prospect is out of our target market.")

determineProspectAgeBracket(17)
determineProspectAgeBracket(45)
determineProspectAgeBracket(65)

"""
Nested Ifs
"""

"""
A nested if is an if statement that is the target of another
if statement.

it checks another condition if a previous condition resolved
to true.

unlike elif which checks another condition if a previous
condition resolved to false.
"""

income_millions = 6

if income_millions >= 100:
    print("This is a high networth individual(HNI).")
    if income_millions >= 500:
        print("This HNI Individual is in the upper band of HNIs.")
    else:
        print("This HNI Individual is in the lower band of HNIs.")
else:
    print("This is not a high networth individual(HNI).")


income_millions = 300

if income_millions >= 100:
    print("This is a high networth individual(HNI).")
    if income_millions >= 500:
        print("This HNI Individual is in the upper band of HNIs.")
    else:
        print("This HNI Individual is in the lower band of HNIs.")
else:
    print("This is not a high networth individual(HNI).")


"""
Let's further break it down to check if customer is middle class
or lower class.
"""

income_millions = 6

if income_millions >= 100:
    print("This is a high networth individual(HNI).")
    if income_millions >= 500:
        print("Customer is in the upper band of HNIs.")
    else:
        print("Customer is in the lower band of HNIs.")

elif income_millions >= 10 and income_millions < 100:
    print("This is a middle class individual.")
    if income_millions >= 50:
        print("Customer is in the upper band of middle class.")
    else:
        print("Customer is in the lower band of middle class.")

else:
    print("This is lower class individual.")


########
income_millions = 75

if income_millions >= 100:
    print("This is a high networth individual(HNI).")
    if income_millions >= 500:
        print("Customer is in the upper band of HNIs.")
    else:
        print("Customer is in the lower band of HNIs.")

elif income_millions >= 10 and income_millions < 100:
    print("This is a middle class individual.")
    if income_millions >= 50:
        print("Customer is in the upper band of middle class.")
    else:
        print("Customer is in the lower band of middle class.")

else:
    print("This is lower class individual.")


"""
EXERCISE: TRY TO PUT THESE CHECKS INTO A FUNCTION.
"""
