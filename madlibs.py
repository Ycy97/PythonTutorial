#string concantenation practice
#example use case : "subscribe to _______";

# print("Fill in the blanks")
# print("Subscribe to ________")

# #user input
# userAns = input("Your Answer :")

# #method 1 
# print("Subscribe to " + userAns)

# #method 2 
# print("Subscribe to {}" .format(userAns))

# #method 3
# print(f"Subscribe to {userAns}")

#variables for user inputs

adj = input("Adjective : ")
verb1 = input("1st Verb : ")
verb2 = input("2nd Verb : ")
famous_person = input("Famous person :")


madlib = f"Machine learning is so {adj}! It makes me so excited because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)