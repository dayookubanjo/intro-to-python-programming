# Identify duplicate elements in a list

import copy

l1 = [10, 15, 25, 10 , 45, 17, 15, 17, 76, 45, 10, 10]
j = copy.deepcopy(l1)

#Empty set to enter unique elements that appeared more than once
lt= set( () )

for i in l1:
    j.remove(i)
    if i in j:
        lt.add(i)

print(lt)


"""
Exercise:

Given a list of fruits in a list, create a function to count the number of each fruit in the list.
print out the fruit and count from the fruit with the highest count down to the fruit with the 
lowest count (descending order).

fruit_basket = ["grape", "orange", "grape", "apple", "orange", "grape", "banana", "mango", "apple"]

Expected result:
"grape, 3" 
"orange, 2" 
"apple, 2" 
"banana, 1" 
"mango, 1" 

"""

print('Exercise starts here \n')

def listBasketCounter(basket_list):
    result_dictionary = {}
    for i in basket_list:
        key = i
        value = basket_list.count(i)
        if key not in result_dictionary:
            result_dictionary[key]=value

    print(result_dictionary)

    # We need to sort the dictionary in order of their value (descending)

    import operator

    sorted_dictionary = sorted(result_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    print (sorted_dictionary)

    for i in sorted_dictionary:
        print( i[0] + "," + " " + str( i[1] ) )
 
        
fruit_basket = ["grape", "orange", "grape", "apple", "orange", "grape", "banana", "mango", "apple"]

listBasketCounter(fruit_basket)


"""
Given an array arr & divisor, get the number of combination of 3 numbers where 
i < j < k and sum of i, j, k is divisible by d.

e.g. 

arr = [2,3,1,6] and d = 2

Result: 
Combinations [1,2,3] and [1,3,6] meet the criteria hence result should be 2 (meaning 2 combinations)
"""

def getTest(arr,d):
    import copy 
    arr2 = copy.deepcopy(arr)
    result = []
    for i in range(0,len(arr)):
        a = arr[i]
        arr2.remove(a)
        for j in range(len(arr2) - 1):
            b = arr2[j]
            c = arr2[j+1]
            if j != 0:
                ff = arr2[j]
                e = arr2[j-1]
                result.append([a,b,c])
                result.append([a,d,e])
            else:
                result.append([a,b,c])
        
        arr2 = copy.deepcopy(arr)
    
    new_result = []
    for z in result:
        if z[0] < z[1] < z[2] and sum(z)%d == 0:
            new_result.append(z)

    final_result = len(new_result)
    return final_result


print( getTest([2,3,1,6], 2) )
