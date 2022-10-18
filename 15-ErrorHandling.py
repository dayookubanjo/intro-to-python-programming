"""
Error handling is used to ensure that when an error occurs in your code, it is handled properly
and it doesnt stop your program


try:
    #code you want to execute or try
except:
    #how you want to handle an error if it occurs

"""

print(xyz)


#############
try:
    print(xyz)
except:
    print("There was an error")

#Code execution wasn't stopped
#Error was handled and an error message returned


###############

#This function converts age in days but there was an error

#a is an int so you can't concatenate with + except u convert to string using str()

def ageindays(age):
    a = age * 365
    print ( "Your age in days is: " + a )
    print("This program still continued after handling the error")

ageindays(23) #TypeError


#Handle a particular type of error (e.g. TypeError)
def ageindays(age):
    try:
        a = age * 365
        print ( "Your age in days is: " + a )
    except TypeError as e:
        print("Error captured: " + str( e ) )
        print("This program continued after handling the error")

ageindays(23)



#Handle all errors and print the error details

def ageindays(age):
    try:
        a = age * 365
        print ( "Your age in days is: " + a )
    except Exception as e:
        print("Error details:" , str( e ) )
        print("This program continued after handling the error")

ageindays(23)
