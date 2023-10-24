set={"apple","banana","cherry"}
set1={1,2,3,4,5}
print(set)
print("cherry"in set)
set.add("Strowberry")
print(set)
set.update(set1)
print(set)
set.remove("banana")
print(set)
set1.discard(4)
print(set1)
set3=set.union(set1)
print(set3,"unioon")
##################################
set2={"apple","banana","cherry"}
set3={"google","microsoft","apple"}
#set2.intersection_update(set3)
print(set2)
set2.symmetric_difference_update(set3)
print(set2)
###
set1={'a','b','c'}
set2={1,2,3}
set3=set1.union(set2)
print(set3)


