# set are catain the collections of data type and also the set are  write in {}
set1 = {1,2,3,4,5,6}
set2 = {1,2,3,4,5,6,7}
print(set1)
print (set2)

# set methods
#union 

set1 = {1,2,3,4,5,6}
set2 = {1,2,3,4,5,6,7}
print (set1|set2)

#intrsection

set1 = {1,2,3}
set2 = {3,4,5,}
print(set1 & set2)

#difference
set1 = {1,2,3}
set2 = {3,4,5,}
print(set1 - set2)

#symetric difference
set1 = {1,2,3}
set2 = {3,4,5,}
print(set1 ^ set2)

#subset

set1 = {1,2,3}
set2 = {1,2,3,4}
print(set1 <= set2)

set1 = {1,2,3}
set2 = {3,4,5,}
print(set1 <= set2)

#super set
set1 = {1,2,3}
set2 = {3,4,5,}
print(set1 >=set2)

set1 = {1,2,3,4}
set2 = {1,2,3}
print(set1 >= set2)

#disjoint return a no common element of both

set1 = {1,2,3}
set2 = {3,4,5,}
print(set1.isdisjoint (set2))

set1 = {1,2,3}
set2 = {4,5,6}
print(set1.isdisjoint(set2))

#add 
set1 = {1,2,3}
set2 = {3,4,5,}
set1.add(5)
print(set1)

#remove
set1 = {1,2,3,5}
set2 = {3,4,5,}
set1.remove(5)
print(set1)

#pop
set1 = {1,2,3}
set2 = {3,4,5,}
set1.pop()
print(set1)


