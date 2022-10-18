"""
For loop is used to loop/iterate through a collection of
elements and execute a statement
"""

"""
Let's first discuss a Python function: range() that is often used
with for loops

#range is used to generate a list of number.

range(start_number, end_number(excluded), increment)

range (0,3,1) = [0,1,2]

range (0,3,1) = range(3) Uses default start_number of 0 and
default increment of 1

"""


list1 = list( range(0,3,1) )
print( list1 )


list2 = list ( range(3) )
print( list2 )


list3 = [10,9,4]

for i in list3:
    print (i)


list4 = [0,1,2] #Equal to range(3)

for i in list4:
    print("I will never lie again.")


"""
use range(x) in a for loop if you want to perform the task
in the for loop "x" amount of time
"""

for i in range(5):
    print("I will never lie again.")


"""
Example:

Given a list of employee salaries, write a for loop
to increase all salaries by 10% and save the new salaries in
another list.

"""

salary = [10, 5 , 34, 64, 76, 19]

#Create an empty list where i'll insert new salaries after calc
new_salary = []

for i in salary: #meaning for each value of salary list
    increase = i * 0.1
    a = i + increase
    new_salary.append(a)

print( new_salary )


"""
What if we want to vary the % to increase the salary based
on the current salary. (5% for >=50, 10% for others )
"""


salary = [10, 5 , 34, 64, 76, 19]

#Create an empty list where i'll insert new salaries after calc
new_salary = []

for i in salary: #meaning for each value of salary list
    if i >= 50:
        increase = i * 0.05 #Increase by 5% if 50 and above
        a = i + increase
        new_salary.append(a)
    else:
        increase = i * 0.1 #Increase by 10% if less than 50
        a = i + increase
        new_salary.append(a)

print( new_salary )



"""
What if the company approved different % increase to salary based
on employee performance.
"""

salary = [10, 5 , 34, 64, 76, 19]
approved_incr = [0.08, 0.1, 0.05, 0.15, 0.13, 0.2]

#Create an empty list where i'll insert new salaries after calc
new_salary = []

indx = 0 #Initialize the first index in approved_incr

for i in salary:
    j = approved_incr[indx]
    increase = i * j
    a = i + increase
    new_salary.append(a)
    indx = indx + 1

print( new_salary )


"""
% is a remainder operator that divides two numbers and
returns the remainder
"""

#Get the list of even numbers and odd numbers between 1 and 50

num_list = list ( range(1,51,1) )

#Empty list where even & odd numbers will be appended
even_list = []
odd_list = []


for i in num_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list)
print(odd_list)
