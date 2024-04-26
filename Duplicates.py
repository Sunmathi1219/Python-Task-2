# find duplicates in three python lists

list1=[11,80,34,45,55]
list2=[45,55,34,71,80]
list3=[55,34,71,80,97]


duplicates=set(list1) & set(list2) & set(list3)

print("Dupicates in the given lists:", duplicates)

