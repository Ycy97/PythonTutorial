#Python Training
#if 5 > 2:
#    print("Five is greater than two!")

#Python Variables
# x = 5
# y = "Cheng Yee"
# print(x)
# print(y)

#Python also has type Casting
# x = str(3)
# y = int(3)
# z = float(3)

# print(x,y,z)

#type of variable can be obtained through type() function
# x = 5
# y = "Cheng Yee"

# print(type(x))
# print(type(y))

#Variable Names
# Rules of Python Variables:
# 1) Must start with letter or underscore character
# 2) Cannot start with a number
# 3) Can only contain alpha-numberic chars and underscore
# 4) Case-sensitive
 
#Accepted format
# 1) Camel Case : myVariableName
# 2) Pascal Case : MyVariableName
# 3) Snake Case : my_variable_name

#Unpack a Collection
# If we have a collection of values in a list, tuple etc, Python allows us to extract the values into variables (known as unpacking)
# fruits = ["apple" , "banana", "cherry"]
# x,y,z = fruits
# print(x,y,z)
# String concatenation works in Python too using + operator
# to print different data type, use comma
# x = 5 
# y = "John"
# print(x,y)

#Global variables are variables that are created outside of a function

# x = "awesome"

# def myFunc():
#     x = "cool"
#     print("Python is "+ x)

# myFunc()

# print("Python is " + x)

#To create a global variable inside a function, use the "global" keyword; usage can be a function that modified global variable value

# def myFunc():
#     global x
#     x = "fantastic"

# myFunc()

# print("Python is totally " + x)

#Slicing in Python
# b = "Hello World!"
# print(b[2:5])
# print(b[:5])
# print(b[2:])
# #Negative indexing, from behind
# print(b[-5:-2])

#Split method in Strings
# a = "Hello ppl in this World!"
# #print(a.split(" "))
# b = a.split(" ")
# print(b[1])

#String format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder2.format(quantity,itemno,price))