#"Strings are arrays, and you can access elements through square brackets"
a = "Hello, World!"
print(a[3])

#Loop through letters
for x in "banana":
  print(x)

#Get the length of a string:
a = "Hello, World!"
print(len(a))

#Check if something is in the text:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Slicing - Changing syntax
#returns from position 2-5(not included)
b = "Hello, World!"
print(b[1:5])
print(b[:5])
print(b[7:])

# Negative indexing to slice from end
b = "Hello, World!"
print(b[-5:-2])

#Modify
print(a.upper()) #Uppercase
print(a.lower()) #Lowercase
print(a.strip()) #Removes space from start/end
print(a.replace("H", "J")) #replaces a part of string
print(a.split(",")) #Splits the word into two from the character

# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#F-Strings
price = 59
txt = f"The price is {price:.2f} dollars" #Round to 2 decimals
print(txt)

# To insert characters that are illegal in a string, use an escape character (a backslash \ followed by the character you want to insert).
txt = "We are the so-called \"Vikings\" from the north."
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace


