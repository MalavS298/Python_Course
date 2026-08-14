#Set items are unordered, unchangeable, and do not allow duplicate values.
#BUT YOU CAN ADD AND REMOVE ITEMS
# The values True and 1/ False and 0 are considered the same value in sets, and are treated as duplicates
# String, int and boolean data types

thisset = {"apple", "banana", "cherry"}
print(len(thisset))  #Get length

#Accessing items workaround
for x in thisset: #Loop
  print(x)

print("banana" in thisset) #Check if present
print("banana" not in thisset) #Check if not present

#Add items
thisset.add("orange")
tropical = ["pineapple", "mango", "papaya"]
thisset.update(tropical) #The .update can combine tuples,lists,and dictionaries with a set

#Remove Items
thisset.remove("banana")
#OR
thisset.discard("banana")
x = thisset.pop() #Remove random item using pop()
thisset.clear() #Clears list
del thisset #Deletes the entire set

#LOOP
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Join Sets
# The union() and update() methods joins all items from both sets.
# The intersection() method store ONLY the repeated values in both sets.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the repeated values.

"Union & Update"
#They will exclude duplicates
set1 = {"a", "b", "c"}
set2 = [1, 2, 3]
set3 = set1.union(set2) #Combine lists-Can union any type: tuple, list, dict.
#OR
set3 = set1 | set2 # You can add how many ever items you want

set1.update(set3) #Extend-Add items from set 3 to set 1

"Intersection"
set3 = set1.intersection(set2)
#OR
set3 = set1 & set2

set1.intersection_update(set2) #Same thing but extends onto 1 instead of creating a new one

"Difference"
set3 = set1.difference(set2)
#OR
set3 = set1 - set2

set1.difference_update(set2) #Same thing but extends onto 1 instead of creating a new one

"Symmetric Differences"
set3 = set1.symmetric_difference(set2)
#OR
set3 = set1 ^ set2

set1.symmetric_difference_update(set2) #Same thing but extends onto 1 instead of creating a new one

#Frozenset is an immutable version of a set. Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.
a = frozenset({"apple", "banana", "cherry"})
b = frozenset({"apple", "pear", "cherry"})

#Same shortcuts and commands as above
c = a.copy() #Returns a copy
d = a.difference(b) # Returns set with the difference
e = a.symmetric_difference(b) #Returns set with symmetric difference
f = a.intersection(b) #Returns new set with intersection
g = a.union(b) #Returns new set with the union



