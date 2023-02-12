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
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity,itemno,price))

# myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}"
# print(myorder2.format(quantity,itemno,price))

#Python Operators
#Arithmetic Operators
# x = 1 + 5
# y = 5 - 1
# a = 5 * 3
# b = 6 / 2
# c = 15 % 4
# d = 2 ** 2
# e = 15 // 7

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(x)
# print(y)

#Membership operators
# x = ["apple", "banana"]
# print("banana" in x)
# print("banana" not in x)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#List in Python
#List items are ordered, changeable, and allow duplicate values.
# myList = ["a" , "b", "c"]
# print(myList)
# myList.append("d")
# print(myList)
# #List length
# print(f"Length of List : {(len(myList))}")
# #A list can contain different data types:
# list1 = ["abc", 34, True, 40, "male"]
# print(list1) 

#Range of indexes
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5+1])


#Check if Item Exists

# list2 = ["apple" , "banana"]

# if "apple" in list2:
#     print("Apple exists in the list!")

#Change Item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist) 

#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# thisList  = ["apple", "banana"]
# thisList.insert(1, "watermelon")
# print(thisList)

# Add item at end of list using append()
# to append anoher list to current list, use extend() method
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)

# list1 = ["apple" , "banana", "cherry"]
# list2 = ["watermelon" , "kiwi"]
# list1.extend(list2)
# print(list1)

# list1 = ["apple" , "banana", "cherry"]
# list2 = [*list1,"watermelon" , "kiwi"]
# print(list2)

#Remove list items
#To remove specified item : remove()

# list1 = ["apple", "banana"]
# list1.remove("banana")
# print(list1)

#To remove specified index : pop()
# list1 = ["apple", "banana", "cherry"]
# list1.pop(1)
# print(list1)

#To clear the list : clear()
# list1 = ["apple", "banana", "cherry"]
# list1.clear()
# print(list1)

#Looping through a list
# thisList = ["apple" , "banana" , "cherry"]
# for x in thisList:
#     print(f"{x} modified")

#Loop through Index Numbers
# thisList = ["apple", "banana", "cherry"]
# for i in range (len(thisList)):
#     print(f"{thisList[i]} printed")

#Python List Comprehension
# List Comprehension offers a shorter syntax when we want to create a new list based on values of existing list
#Syntax : newlist = [expression for item in iterable if condition == True]
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

#Python Sort
# sort() : alphanumerically ascending by default
# thisList = ["orange", "cherry", "banana", "apple"]
# thisList.sort()
# print(thisList)

#sort descending using parameter reverse=True
# thisList = ["orange", "cherry", "banana", "apple"]
# thisList.sort(reverse=True)
# print(thisList)

#Case insensitive sort
# thisList = ["banana", "Orange", "Kiwi", "cherry"]
# thisList.sort(key=str.lower)
# print(thisList)

#To reverse list without sorting order : reverse()
# thisList = ["banana", "Kiwi", "Orange", "cherry"]
# thisList.reverse()
# print(thisList)

#Copy list 
#copy(), list()

# thisList = ["chicken", "dog", "cat"]
# thisList2 = thisList.copy()
# print(thisList2)

#Python Tuples
#Tuples are unchangeable, we cannot change add or remove items after the tuple has been created (immutable)
# thisTuple =  ("apple", "banana", "cherry", "apple", "cherry")
# print(thisTuple)

#Tupple is accessed by referring to index number

# thisTuple = ("apple", "banana")
# print(thisTuple[1])

#unpacking / destructuring tupple
# fruits = ("apple", "banana", "cherry")

# (item1, item2, item3) = fruits

# print(item1, item2, item3)

#Asterisk *
#assigning values to variable as a list

# fruits = ("apple", "banana","cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

#if asterisk added to another var than the last, python will assign accordingly to match values and variables left
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)

#Python Sets
#unordered, unchangeable (but can add new item), no dups allowed
# thisSet = {"apple", "banana", "apple"}
# print(thisSet)

#Accessing items in set; cannot use index or key
# import this


# thisSet =  {"apple","banana","cherry"}
# for x in thisSet:
#     print(x)

#Adding item to set
# thisSet =  {"apple","banana","cherry"}
# thisSet.add("orange")
# print(thisSet)

#To add items from another set into the current set : update()
# thisSet =  {"apple","banana","cherry"}
# mySet = {"kiwi","watermelon"}
# thisSet.update(mySet)
# print(thisSet)

#Remove items from set : remove() / discard() ; discard() will not raise error if value doesnt exist

# thisSet =  {"apple","banana","cherry"}
# thisSet.discard("kiwi")
# print(thisSet)

#looping through a set
# thisSet = {"apple","banana","cherry"}

# for x in thisSet:
#     print(f"{x} accessed")

#Python sets follows mathematic's method : union(), intersection() 

#Python Dictionaries
#Dictionaries are used to store data values in key:value pairs
# thisDict = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1964
# }

#print(thisDict)

#Access dictionary through key names
# print(thisDict["brand"])

#or through get() function
# print(thisDict.get("model"))

# x = thisDict.keys()
#print(x)
# for y in x:
#     print(y)

#getting all values in dictionary
# x = thisDict.values()
# print(x)

#get items : items() for returning key:value pairs
# y = thisDict.items()
# print(y)

#to modify value of selected key
# g = thisDict["model"]
# print(f"{g} is the prev value")
# thisDict["model"] = "Perodua"
# print(thisDict["model"] ,"is the new value")

#Adding new item to dictionary
# thisDict["color"] = "red"
# print(thisDict)

#Nested Dictionaries

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily)

#Python if else
# a = 456
# b = 456

# if b > a:
#     print("b is greater than a")
# elif b==a:
#     print("b is equal to a")
# else:
#     print("b is smaller than a")


#Python while loops

# i = 1
# while i < 6:
#     print(i)
#     i+=1

#else statement while loop
# i = 1
# while i < 6:
#     print(i)
#     i+=1
# else:
#     print("i is larger or equal than 6")

#Python For Loops
# for x in "banana":
#     print(x)

#Range function
#range() returns a sequence of numbers starting from 0 by default and increments by 1
# for x in range(2,6):
#     print(x)

#to control increment value add in 3rd parameter
# for x in range (2, 20, 3):
#     print(x)

#Nested for loops

# adj = ["red", "big", "tasty"]
# fruits = ["orange", "apple", "banana"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

#pass statement, if for loops has no content

# for x in [0,1,2]:
#     pass

#Python Functions
#function is defined using the def keyword

# def my_function(x):
#     print(f"Hello from {x}")

# my_function("Hell")
# my_function("Heaven")
# my_function("Earth")

#Arbitary arguments , *args

# def my_function(*kids):
#     print(f"The youngest child is {kids[2]}")

# my_function("Emil","Tobias","Linus")

#Keyword Arguments
# def my_function(child3, child2, child1):
#     print(f"The youngest child is {child3}")


# my_function(child1="Emil", child2="Tobias", child3="Linus")

#Arbitary Keyword Arguments, **kwargs
#if do not knw hw many keyword arguments that will be passed, add two asterisk before the parameter name in the f(x) definition
#this way the f(x) will receive a dictionary of arguments and can access them accordingly

# def my_function(**kid):
#     print(f"His name is {kid['lname']}")

# my_function(fname="Tobias", lname="Knicks")

#Default parameter val
#if we call function without argument, it uses default value

# def my_function(country="Norway"):
#     print(f"I am from {country}")

# my_function("Holland")
# my_function()
# my_function("Malaysia")

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

#Python Lamda
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

# x = lambda a: a+10
# print(x(5))

#Lambda can take in any number of arguments
# x = lambda a,b: a * b

# print(x(5,6))

#Python Class

# class MyClass:
#     x = 5

# p1 = MyClass()

# print(p1.x)

#Python has built in __init__() function which will always execute when the class is being initiated
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def myFunction(self):
#         print(f"Hello my name is {self.name}")

# p1 = Person("John", 36)
# # print(p1.name)
# # print(p1.age)
# p1.myFunction()

#Python Inheritance

#Parent Class
# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printName(self):
#         print(self.firstname, self.lastname)

# p1 = Person("John", "Doe")
# p1.printName()

# #Child Class
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

#     def welcome(self):
#         print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

# x = Student("Cheng", "Yee", 2022)
# x.welcome()