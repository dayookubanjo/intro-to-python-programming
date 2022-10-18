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