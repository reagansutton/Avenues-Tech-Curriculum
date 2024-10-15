# lists and strings

# strings
s = "My name is Arthur."
print("s=", s)
print("s[[0]=", s[0]) # s[0] is the M
print("s[[8]=", s[8]) # s[8] is the i (count from 0 including spaces)
print("length of s is", len(s))
print("last char in s is", s[len(s)-1]) # the period is the last character
print("s[2,9]=", s[2:9]) # list the characters from 2-8
print("s[:9]=", s[:9]) # stops at 8
print("s[2:]=", s[2:]) # starts at 2 and goes until the end

"""
# lower
choice = "x"
while choice != "q" # and choice != "Q":
    print("stuff")
    choice = input("...a b c...q :").lower() #makes everything lower case
# can use lower on Lab 5

"""

"""
ageStr = input("How old are you? ")
while not ageStr.isdigit(): # if they do not type in a digit make them answer again
    ageStr = input("How old are you? ")
age = int(ageStr)
print("Twice your age is", 2*age)

"""

# lists

fruit = ["banana", "apple", "orange", "grape", "kiwi"]
print("fruit=", fruit) # printing entire list

for piece in fruit:
    print("piece=", piece) #printing one item at a time

print("fruit[0]=", fruit[0])
print("fruit[2:4]=", fruit[2:4]) # fruits number 2-3

print("about to add peach")
fruit.append("peach") # add peach to the list
print("fruit=", fruit)

print("about to remove apple")
fruit.remove("apple") # remove apple from the list
print("fruit=", fruit)

print("remove orange by number") # orange is number 1
del fruit[1] # delete fruit 1
print("fruit=", fruit)

print("where is grape (index?")
grapeIndex = fruit.index("grape") # what number is grape
print("grapeIndex=", grapeIndex)

print("try to remove mango")
if "mango" in fruit: # need to add this so program doesn't crash
    fruit.remove("mango") # program crashes because mango is not there
    print("fruit=", fruit)

import random # this is how you let random function work

for i in range (10):
    print("random fruit =", random.choice(fruit)) # pick a random option from the list

fruitAgain = fruit[:]
fruitAgain.remove("banana")
print("fruitAgain =", fruitAgain)
print("fruit=", fruit) # includes banana

