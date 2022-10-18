"""
while loops are used to continiously execute a block of statements
while a condition is true.

it only stops when the condition becomes false

BE VERY CAREFUL WITH WHILE LOOPS BECAUSE IT CAN RESULT IN AN
INFINITE LOOP WHICH CAN MAX OUT YOUR COMPUTERS RESOURCES
"""

#DANGER: THIS WILL RESULT IN AN INFINITE LOOP SO BE VERY CAREFUL

a = 5
while a > 3:
    print(a)


a = 5
while a > 3:
    print(a)
    a = 0 #break condition
#Give it a break conditn to make the while loop false and stop


#You can also just add a break command to break the loop
a= 5
while a >= 0:
    print(a)
    break #breaks the  loop


#Use while loop to print from a number down to 0
a = 15
while a >= 0:
    print(a)
    a = a - 1
