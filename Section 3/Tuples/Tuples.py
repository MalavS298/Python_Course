# Tuples are unchangeable
#String, int and boolean data types

myTuple = ("apple", "banana", "cherry", "grape", "orange")
print(len(myTuple)) #Find the length

thisTuple = ("apple",) #need a comma for a single item to be considered as a tuple

print(myTuple[1]) #Print second item

print(myTuple[1:3]) #Index Tuples like lists

#You can convert a tuple to a list, then change/remove an item from the list, and then convert back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi" # Change
y.remove("cherry") # Remove
x = tuple(y)
print(x)

#Add items by converting the item to a tuple and then combining them
tupleConvert = ("apple", "banana", "cherry")
y = ("orange",)
tupleConvert += y

del tupleConvert #Though deleting the whole tuple is allowed

#Unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits #Green = Apple, Yellow = Banana, etc.

fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *tropic, red) = fruits #Asterisk declares to give the necessary values to it. here green = apple, red = rasberry and else = tropic

#Joining
tuple3 = fruits + fruits2 #Join Tuples
myMultiply = fruits * 2 #Multiply it
print(tuple3)


#Looping
for x in fruits2: #Classic
  print(x)

thistuple = ("apple", "banana", "cherry") #Go through Tuple
for i in range(len(thistuple)):
  print(thistuple[i])

#OR

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#Methods
# count():	Returns the number of times a specified value occurs in a tuple
# index():	Searches the tuple for a specified value and returns the position of where it was found

