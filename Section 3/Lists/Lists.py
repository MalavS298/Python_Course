#Ternary
num = 10
x = "WEEKEND!" if num > 5 else "Workday"
#Review Bitwise operators

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# *Set items are unchangeable, but you can remove and/or add items whenever you like.

"List"
list1 = [1]
list2 = [2]
mylist = [1,2,3,4,5]
thislist = ["Apple", 5 , "Malav"] #Defining a list with[]
new = list(thislist) #assigning a set list

thislist[1] = 6 #Change a value/range of values
thislist.insert(2, "watermelon") #Insert an object in between the list

thislist.append("orange") #Add an item
mylist.extend(thislist) #Combine lists

thislist.remove("orange") #Remove Item
thislist.pop(1) #Removes item via # Index
del thislist[0] #Delete/Remove like this too
del thislist #Delete the whole list

pool = [x for x in thislist] #Cycle through without doing for x in x...

thislist.sort() #Sort the list alphanumerically
thislist.sort(reverse = True) #Sort descending order
thislist.reverse() #Reverses current elements
thislist.sort(key = str.lower) #Case-sensitive so often make it lowercase first

mylist = thislist.copy() #You can duplicate a list

list3 = list1 + list2 #Combine like this too






