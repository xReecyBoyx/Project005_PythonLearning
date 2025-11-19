from datetime import datetime, date, time, timedelta
import math
import random

# INTRO
print("My Name is Reece")
print("Hello World!")

# VARIABLES
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
print("This is an upper case string.".upper())
print("This is a lower case string.".lower())
print("IS THIS UPPER".isupper())
print("is this upper".isupper())

apexCharacter1 = "Bangalore"
apexCharacter2 = "Lifeline"
apexCharacter3 = "Gibraltar"

# string literal
print(f"The first character in the character list is {apexCharacter1}.")
print(f"The second character in the character list is {apexCharacter2}.")

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

myFirstRandomNumber = random.randint(1,6)
mySecondRandomNumber = random.randint(1,6)
print("RANDOM")
print(f"My first random number is {myFirstRandomNumber}")
print(f"My second random number is {mySecondRandomNumber}")

# COLLECTIONS
# Lists
friends = ["Jason Wheelan", "Reece Hillier", "Macaulay Curt", "Amy Windsor"]
print("My first friend is ")

