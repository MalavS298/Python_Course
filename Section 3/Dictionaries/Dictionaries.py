#Dstore data values in key:value pairs.
#collection which is ordered*, changeable and do not allow duplicates.
#duplicate value will overwrite existing
#Can hold any value

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"]) #Print the value of the key
print(len(thisdict)) #Number of keys

x = thisdict["model"] #get value of key
y = thisdict.keys() #get list of all keys
z = thisdict.values() #get list of all values
a = thisdict.items() #get list of all key:value pairs

thisdict["year"] = 2018 #Change a given value
#OR
thisdict.update({"year": 2020}) #Update the "year" with update() method:

thisdict["color"] = "red" #ADD VALUE
#OR
thisdict.update({"color": "red"})

thisdict.pop("model") #REMOVE VALUE
#OR
del thisdict["model"]

thisdict.clear() #EMPTY DICTIONARY
del thisdict #DELETE DICTIONARY

"Loop"
for x in thisdict: #print all key names
  print(x)
#OR
for x in thisdict.keys():
  print(x)

for x in thisdict: #print all value names
  print(thisdict[x])
#OR
for x in thisdict.values():
  print(x)

for x, y in thisdict.items(): #loop both keys and values
  print(x, y)

"Copy"
mydict = thisdict.copy() #copy a dict
#OR
mydict2 = dict(thisdict)

"Nested"
myFamily = { #One dictionary with 3 dictionaries
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {  #Combine 3 dict into one
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"]) #print name of child #2

for x, obj in myfamily.items(): #Loop through keys and values of nested dict.
  print(x)

  for y in obj:
    print(y + ':', obj[y])














