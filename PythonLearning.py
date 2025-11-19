from datetime import datetime, date, time, timedelta
import math
import random

# INTRO
print("INTRODUCTION - HELLO WORLD")
print("--------------------------")
print("My Name is Reece")
print("Hello World!")

# VARIABLES
print("VARIABLES")
print("---------")
firstName = "Reece"
surname = "Hillier"
dateOfBirth = "19/09/1993"
mainCharacter = "Bangalore"
favColor = "Teal"
favFood = "Chicken Tikka Massala"
age = 32
moneyInBank = 4032.12
isMale = True

# Story with conversion
print("There once was a man named " + firstName + " " + surname + ".")
print(firstName + "'s date of birth was " + dateOfBirth + ", making him " + str(age) + " years old.")
print(firstName + "'s favourite food was " + favFood + ". His favourite color was " + favColor + ".")
print(firstName + " enjoys Apex Legends and he mains " + mainCharacter + ".")
print(firstName + " " + surname + " was not rich and had £" + str(moneyInBank) + " in the bank.")

# STRINGS
print("STRINGS")
print("-------")
print("This is an upper case string.".upper())
print("This is a lower case string.".lower())
print("IS THIS UPPER".isupper())
print("is this upper".isupper())
print(" ")

apexCharacter1 = "Bangalore"
apexCharacter2 = "Lifeline"
apexCharacter3 = "Gibraltar"

# string literal
print(f"The first character in the character list is {apexCharacter1}.")
print(f"The second character in the character list is {apexCharacter2}.")
print(" ")

# character array
print("Character index")
print(f"character 1: {apexCharacter1[0].upper()}")
print(f"character 2: {apexCharacter1[2].upper()}")
print(f"character 3: {apexCharacter1[3].upper()}")
print(f"character 6: {apexCharacter1[6].upper()}")

# substring
oldPlace = "WD18 7LY"
newPlace = "CM1 3GU"

oldSpace = oldPlace.find(" ")
newSpace = newPlace.find(" ")

oldPlaceLeft = oldPlace[0:(oldSpace)]
newPlaceLeft = newPlace[0:(newSpace)]

oldPlaceRight = oldPlace[(oldSpace+1):(len(oldPlace))]
newPlaceRight = newPlace[(newSpace+1):(len(newPlace))]

print(" ")
print("ORIGINAL")
print("--------")
print(f"Old Postcode: {oldPlace}")
print(f"New Postcode: {newPlace}")
print(" ")

print("SPACE INDEX")
print("--------")
print(f"Old Postcode Space Index: {str(oldSpace)}")
print(f"New Postcode Space Index: {str(newSpace)}")
print(" ")

print("LEFT POSTCODE")
print("--------")
print(f"Left Part of Old Postcode: {oldPlaceLeft}")
print(f"Left Part of New Postcode: {newPlaceLeft}")
print(" ")

print("RIGHT POSTCODE")
print("--------")
print(f"Right Part of Old Postcode: {oldPlaceRight}")
print(f"Right Part of New Postcode: {newPlaceRight}")
print(" ")

# NUMBERS
print("NUMBERS")
print("-------")
myNumb = 2
print(f"My Numb: {str(myNumb)}")

myNegNumb = -6
print(f"My Negative Numb: {str(myNegNumb)}")
print(f"My Negative Numb Absolute: {str(abs(myNegNumb))}")
print(" ")

print("Basic Math Ops")
print("--------------")

myBasicMathOp = 3 + 4
print(f"3 + 4 = {str(myBasicMathOp)}")

myBasicMathOp = 3 - 4
print(f"3 - 4 = {str(myBasicMathOp)}")

myBasicMathOp = 3 * 4
print(f"3 * 4 = {str(myBasicMathOp)}")

myBasicMathOp = 3 / 12
print(f"3 / 4 = {str(myBasicMathOp)}")

myAdvancedMathOp = 3 + 3 * 4
print(f"3 + 3 * 4 = {str(myAdvancedMathOp)}")

mySquaredMathOp = pow(3, 4)
print(f"3 ^ 4 = {str(mySquaredMathOp)}")
print(" ")

pi = math.pi
print(f"Pi is: {str(pi)}")
print(" ")

exp = math.exp(1)
print(f"Exp is: {str(exp)}")
print(" ")

myFirstRandomNumber = random.randint(1,6)
mySecondRandomNumber = random.randint(1,6)
print("RANDOM")
print("------")
print(f"My first random number is {myFirstRandomNumber}")
print(f"My second random number is {mySecondRandomNumber}")
print(" ")

# COLLECTIONS
# Lists
print("LISTS")
print("-----")
friends = ["Jason Wheelan", "Reece Hillier", "Macaulay Curt", "Amy Windsor"]
print("Original Friends")
print("----------------")
print(f"My friends are {friends}")
print(f"My first friend is {friends[0]}")
print(f"My second friend is {friends[1]}")
print(f"My third friend is {friends[2]}")
print(f"My fourth friend is {friends[3]}")
print(f"I have {len(friends)} total friends.")
print(" ")

print("You can mix data types within lists.")
mixCollection = ["Reece Hillier", 32, "19/09/1993", 6]
print(f"The mixed collection for Reece Hillier is {mixCollection}")
print(f"Name: {mixCollection[0]}")
print(f"Age: {mixCollection[1]}")
print(f"DoB: {mixCollection[2]}")
print(f"Favourite number: {mixCollection[3]}")
print(" ")

newFriends = ["Jim Jones", "Hally Berry", "Mia Solkova", "Emma Watson"]
friends.extend(newFriends)
print("I Made New Friends")
print("------------------")
print(f"My first friends is {friends[0]}")
print(f"My second friend is {friends[1]}")
print(f"My third friend is {friends[2]}")
print(f"My fourth friend is {friends[3]}")
print(f"My fifth friend is {friends[4]}")
print(f"My sixth friend is {friends[5]}")
print(f"My seventh friend is {friends[6]}")
print(f"My eigth friend is {friends[7]}")
print(f"I now have {len(friends)} total friends.")
print(" ")

fruits = ["Orange", "Banana", "Strawberry"]
print("FRUITS")
print("------")
print(f"My first fruit is {fruits[0]}")
print(f"My second fruit is {fruits[1]}")
print(f"My third fruit is {fruits[2]}")
print(" ")
print("I'm adding 3 new fruits to my list.")
print(" ")

fruits.insert(0, "Apple")
fruits.insert(3, "Watermelon")
fruits.insert(4, "Kiwi")

print(f"My first fruit is {fruits[0]}")
print(f"My second fruit is {fruits[1]}")
print(f"My third fruit is {fruits[2]}")
print(f"My fourth fruit is {fruits[3]}")
print(f"My fifth fruit is {fruits[4]}")
print(f"My sixth fruit is {fruits[5]}")
print(" ")

print("I don't like one of my fruits, I am going to remove this fruit.")
print("I don't like watermelon.")
print(" ")

fruits.remove("Watermelon")
print(f"My first fruit is {fruits[0]}")
print(f"My second fruit is {fruits[1]}")
print(f"My third fruit is {fruits[2]}")
print(f"My fourth fruit is {fruits[3]}")
print(f"My fifth fruit is {fruits[4]}")
print(" ")

print("I can also pop from a list at a given index.")
print("I don't like the 3rd fruit in my list.")
print(" ")

fruits.pop(2)
print(f"My first fruit is {fruits[0]}")
print(f"My second fruit is {fruits[1]}")
print(f"My third fruit is {fruits[2]}")
print(f"My fourth fruit is {fruits[3]}")
print(" ")

print("I can get the index of an item in a list.")
print("Get me the index of Orange.")
print(" ")

orangeIndex = fruits.index("Orange")
print(f"Orange is located at the {orangeIndex} position in my fruit list.")
print(" ")

print("I can sort my list alphabetically.")
fruits.sort()
print(f"Fruits: {fruits}")
print(" ")

print("I can specify a descending sort also.")
fruits.sort(reverse=True)
print(f"Fruits: {fruits}")
print(" ")

print("I can clear a whole list quickly and efficiently.")
fruits.clear()
print(f"Fruits after clear: {fruits}")
print(" ")

# TUPLES
print("TUPLES")
print("------")
basicTuple = ("Reece Hillier", 32)
print(f"My first tuple: {basicTuple}")
print(f"The first item in my first tuple is {basicTuple[0]}")
print(f"The second item in my first tuple is {basicTuple[1]}")
print(" ")

# FUNCTIONS
print("BASIC FUNCTIONS")
print("---------------")
def sayHi():
    print("Hi There")

def sayHiToPerson(name):
    print(f"Hi There {name}")

def offerPersonFruit(name, fruitName):
    print(f"Hi there {name}, would you like a {fruitName}?")

print(f"My first function: {sayHi}")
sayHi()
sayHiToPerson("Reece Hillier")
offerPersonFruit("Reece Hillier", "Strawberry")
print(" ")

def Add(firstNumb, secondNumb):
    return firstNumb + secondNumb

def Subtract(firstNumb, secondNumb):
    return firstNumb - secondNumb

def Multiply(firstNumb, secondNumb):
    return firstNumb * secondNumb

def Divide(firstNumb, secondNumb):
    return firstNumb / secondNumb

def Square(number):
    return pow(number, 2)

print("Math ops via a function")
print("-----------------------")
firstNumber = 6
secondNumber = 3

print(f"My first number for math ops is {firstNumber}")
print(f"My second number for math ops is {secondNumber}")
print(" ")
print(f"{firstNumber} + {secondNumber} = {Add(firstNumber, secondNumber)}")
print(f"{firstNumber} - {secondNumber} = {Subtract(firstNumber, secondNumber)}")
print(f"{firstNumber} * {secondNumber} = {Multiply(firstNumber, secondNumber)}")
print(f"{firstNumber} / {secondNumber} = {Divide(firstNumber, secondNumber)}")
print(f"{firstNumber} squared = {Square(firstNumber)}")
print(" ")

threshold = 10
def checkThreshold(number): 
    if (number <= threshold and number >= 0) :
        return True
    elif (number < 0) :
        return False
    elif (number > threshold) :
        return False
    else :
        return None

print("Checking whether number exists in a threshold.")  
print(f"The range for the threshold is {0} to {threshold}")
print(f"Does 6 exist in the threshold: {str(checkThreshold(6)).upper()}")
print(f"Does 16 exist in the threshold: {str(checkThreshold(16)).upper()}")
print(" ")

def isEven(number) :
    if number % 2 == 0 :
        return True
    else :
        return False
    
print("Checking even numbers")
number1 = random.randint(0, 10)
number2 = random.randint(0, 100)
number3 = random.randint(0, 1000)

print(f"The first number is {number1}, is it even? {str(isEven(number1)).upper()}")
print(f"The second number is {number2}, is it even? {str(isEven(number2)).upper()}")
print(f"The third number is {number3}, is it even? {str(isEven(number3)).upper()}")
print(" ")



    

