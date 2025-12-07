from datetime import datetime, date, time, timedelta
import math
import random
import csv
import enum

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

# IF ELIF ELSE
print("BASIC IF ELSE")
print("---------------")
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

# DICTIONARIES
print("DICTIONARIES")
print("------------")
print(" ")
NewPerson = {
    "firstName": "Reece",
    "surname": "Hillier",
    "dob": "19/09/1993",
    "gender": "Male",
    "age": 32,
    "mainCharacter": "Bangalore",
    "favColor": "Teal",
}

OtherPerson = {
    "firstName": "Amy",
    "surname": "Welling",
    "dob": "11/02/1994",
    "gender": "Female",
    "age": 31,
    "mainCharacter": "Horizon",
    "favColor": "purple",
}

def WriteStory(person):
    print(f"There once was a person named {person["firstName"]} {person["surname"]}.")
    print(f"This person was born on {person["dob"]}, they are {person["age"]} years old.")
    print(f"They are the gender of: {person["gender"]}.")
    print(f"Their ain Apex Legends character is {person["mainCharacter"]}.")
    print(f"Their favourite color is {person["favColor"]}.")

print("Writing a story for a person.")
print("-----------------------------")
WriteStory(NewPerson)
print(" ")
WriteStory(OtherPerson)
print(" ")

print("You can safely attempt to retrieve keys from a dictionary")
print(f"The person favourite food is: {NewPerson.get("favFood", "This person has no food preference.")}")
print(" ")

# LOOPS
print("LOOPS")
print("-----")
print("Loops are extremely useful for looping collections or performing repetetive tasks.")
print(" ")

print("WHILE LOOP")
print("----------")
print("While loops iterate while a condition is met.")
print("You must be careful with while loops to not implement an infinite loop.")
print(" ")

print("Implementing a basic while loop from 1 to 10")
i = 1
while i <= 10 :
    print(f"i: {i}")
    i += 1

def LoopWhile(startNumb, endNumb, increment):
    if (startNumb > endNumb) :
        print("Your start number is greater than your end number")
        return
    
    print(f"Looping between {startNumb} and {endNumb} on an increment of {increment}.")
    i = startNumb
    while (i <= endNumb) :
        print(f"i: {i}")
        i += increment
    

print(" ")
LoopWhile(1, 20, 1)
print(" ")
LoopWhile(20, 1, 1)
print(" ")
LoopWhile(100, 1000, 26)
print(" ")

def RollToSix(maxAttempts) : 
    print("Beginning to roll untill retrieving a 6.")
    diceRolls = 0
    rolledYet = False   
    while(not rolledYet) :
        
        numberRolled = random.randint(1, 6)
        diceRolls += 1

        if (diceRolls > maxAttempts) :
            print(f"You didn't manage to roll a 6 in {maxAttempts} attempts.")
            return None
              
        if (numberRolled == 6) :
            print(f"You rolled a 6 after {diceRolls} attempts")
            rolledYet = True
            return diceRolls
        
print("Rolling to 6 function")
print("---------------------")
RollToSix(10)
print(" ")
RollToSix(100)
print(" ")
RollToSix(1000)
print(" ")

print("FOR LOOP")
print("----------")
print("For loops in python are used to traverse collections and lists.")
print(" ")

def getPerson(name, age, gender) :
    return {
        "name": name,
        "age": age,
        "gender": gender
    }

personOne = getPerson("Reece Hillier", 32, "Male")
personTwo = getPerson("James Hendricks", 29, "Male")
personThree = getPerson("Hailey Cummings", 41, "Female")

personCollection = [personOne, personTwo, personThree]
print("I have a collection of people.")

def PrintPeoplesNames(personCollection) :
    i = 0
    for person in personCollection :
        i += 1
        print(f"Person {i}'s name is: {person["name"]}")

def PrintSpecificGender(personCollection, gender):
    print(f"Printing names for the gender: {gender}.")
    i = 0
    for person in personCollection :
        if (person["gender"] == gender) :
            i += 1
            print(f"Person {i}'s name is {person["name"]}, their age is {person["age"]}.")
    
PrintPeoplesNames(personCollection)
print(" ")
PrintSpecificGender(personCollection, "Male")
print(" ")
PrintSpecificGender(personCollection, "Female")
print(" ")

print("You can loop through characters in a string.")
for letter in "Reece Hillier":
    print(letter)

print(" ")

def FindCharacterIndexString(substring, string) :
    print(f"Finding '{substring}' within '{string}'.")
    
    subLength = len(substring)
    mainLength = len(string)
    currentLetter = 0

    for letter in string :
        if ((currentLetter + subLength) > mainLength) :
            print("Could not find the substring within the string.")
            return None
        
        if (string[currentLetter:(currentLetter + subLength)] == substring) :
            print(f"Found the substring at index: {currentLetter}")
            return currentLetter
        
        currentLetter += 1

print("Find a substring via a custom method.")
FindCharacterIndexString("anga", "Bangalore")
print(" ")
FindCharacterIndexString("Salt", "Apatostatic")
print(" ")

print("You can swiftly loop through a range to perform a task.")
for i in range(0, 10):
    print(f"i: {i + 1}")
print(" ")

def CustomPower(base, power) :
    print(f"Calculating {base}^{power}...")

    if power < 0:
        return 1 / CustomPower(base, -power)
    elif power == 0:
        return 1
    else:
        result = base
        if power == 1:
            return base

        for i in range(1, power):
            result = result * base
        
        return result

print(f"3^3 = {CustomPower(3, 3)}")
print(" ")
print(f"4^6 = {CustomPower(4, 6)}")
print(" ")

# NESTED LOOPS
print("NESTED LOOP")
print("----------")
print("You can nest loops.")
print(" ")

nestedList = [
    [3, 7, 13],
    [12, 16, 1],
    [23, 4, 77],
    [12, 13, 11]
]

print(f"My nested list as follows: {nestedList}")
print("Attempting to sum through the nested list.")
curSum = 0
rowIndex = 0
for i in nestedList :  
    rowIndex += 1  
    colIndex = 0
    for j in i :   
        colIndex += 1
        print(f"Summing at row {rowIndex}, col {colIndex}.")
        curSum += j
        print(f"Cumulative Sum: {curSum}")

print(f"The final sum is: {curSum}")
print(" ")

# TRY EXCEPT
print("TRY EXCEPT")
print("----------")
print("You can try and execute something safely while falling back upon an error.")
print(" ")

def tryConvertInt(number) :
    try :
        newInt = int(number)
        print(f"Successfully converted {number} to an integer, the result is {newInt}.")
        return newInt
    except:
        print(f"Failed converting {number} to an integer.")
        return None
    
tryConvertInt("THIS IS NOT A NUMBER")
tryConvertInt("6")
tryConvertInt(6.22)
print(" ")

# READ FILES
print("READ FILES")
print("----------")
print("You can read and manipulate files via Python.")
print(" ")

fileName = "ApexLegendsData.csv"
apexCsv = open(fileName, "r", encoding="utf-8-sig")

print("Below is the first row of the read file.")
print("----------------------------------------")
print(f"Beginning to read {fileName}")
print(f"Reading the first line of {fileName}")
print(" ")
firstRow = apexCsv.readline()
print(firstRow)
print(" ")

print(f"Reading the second line of {fileName}")
print(" ")
secondRow = apexCsv.readline()
print(secondRow)
print(" ")

apexCsv.close()

print("You can read all lines at once from files also into an Array.")
apexCsv = open(fileName, "r", encoding="utf-8-sig")
apexLines = apexCsv.readlines()
print("Reading the 1st and 22nd line from the Apex dataset.")
print(" ")
print(apexLines[0])
print(" ")
print(apexLines[21])
print(" ")
apexCsv.close()
print("You can read Csvs aswell easily using built in packages.")
print(" ")

def ReadApexData(fileName, numberRecs): 
    apexCsv = open(fileName, "r", encoding="utf-8-sig")
    reader = csv.reader(apexCsv)
    apexData = []
    rowCount = 0

    lateAdditions = {
        "hotZone": False,
        "jumpmaster": False,
        "lowLevel": False,
        "tmRankedBadge": False,
        "tmKillsBadge": False
    }

    try :
        for i, row in enumerate(reader):
            if (numberRecs != None and i > (numberRecs + 1)):
                break

            if (i > 1) :
                apexGame = ReadApexRow(row, lateAdditions)
                apexData.append(apexGame)
                rowCount += 1
    except Exception as e:
        print(f"There was an error retrieving the data: {e}")
        return apexData
    
    print(f"Sucessfully retrieved {rowCount} records from the Apex Dataset")
    apexCsv.close()
    return apexData

def GetCharacterDetail(characterName) :
    
    lowerName = characterName.lower()
    if (lowerName == "bangalore") :
        return {
            "SeasonReleased": 0,
            "LegendClass": "Assault",
            "HasCoverGen": True,
            "HasDamageDeal": True,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "bloodhound") :
        return {
            "SeasonReleased": 0,
            "LegendClass": "Recon",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": True,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "caustic") :
        return {
            "SeasonReleased": 0,
            "LegendClass": "Controller",
            "HasCoverGen": False,
            "HasDamageDeal": True,
            "HasFortify": True,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "gibraltar") :
        return {
            "SeasonReleased": 0,
            "LegendClass": "Support",
            "HasCoverGen": True,
            "HasDamageDeal": True,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": True,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "lifeline") :
        return {
            "SeasonReleased": 0,
            "LegendClass": "Support",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": True,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "mirage") :
        return {
            "SeasonReleased": 0,
            "LegendClass": "Support",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": True,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "pathfinder") :
        return {
            "SeasonReleased": 0,
            "LegendClass": "Skirmisher",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": True
        }
    elif (lowerName == "wraith") :
        return {
            "SeasonReleased": 0,
            "LegendClass": "Skirmisher",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "octane") :
        return {
            "SeasonReleased": 1,
            "LegendClass": "Skirmisher",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": True
        }
    elif (lowerName == "wattson") :
        return {
            "SeasonReleased": 2,
            "LegendClass": "Controller",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": True,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "crypto") :
        return {
            "SeasonReleased": 3,
            "LegendClass": "Recon",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": True,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "revenant") :
        return {
            "SeasonReleased": 4,
            "LegendClass": "Skirmisher",
            "HasCoverGen": False,
            "HasDamageDeal": True,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": False
        }
    elif (lowerName == "loba") :
        return {
            "SeasonReleased": 5,
            "LegendClass": "Support",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": False
        }
    elif (lowerName == "rampart") :
        return {
            "SeasonReleased": 6,
            "LegendClass": "Controller",
            "HasCoverGen": True,
            "HasDamageDeal": True,
            "HasFortify": True,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "horizon") :
        return {
            "SeasonReleased": 7,
            "LegendClass": "Skirmisher",
            "HasCoverGen": False,
            "HasDamageDeal": True,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": True
        }
    elif (lowerName == "fuse") :
        return {
            "SeasonReleased": 8,
            "LegendClass": "Assault",
            "HasCoverGen": False,
            "HasDamageDeal": True,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "valkyrie") :
        return {
            "SeasonReleased": 9,
            "LegendClass": "Skirmisher",
            "HasCoverGen": False,
            "HasDamageDeal": True,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": True
        }
    elif (lowerName == "seer") :
        return {
            "SeasonReleased": 10,
            "LegendClass": "Recon",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": True,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": True
        }
    elif (lowerName == "ash") :
        return {
            "SeasonReleased": 11,
            "LegendClass": "Assault",
            "HasCoverGen": False,
            "HasDamageDeal": True,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": True
        }
    elif (lowerName == "maggie") :
        return {
            "SeasonReleased": 12,
            "LegendClass": "Assault",
            "HasCoverGen": False,
            "HasDamageDeal": True,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "newcastle") :
        return {
            "SeasonReleased": 13,
            "LegendClass": "Support",
            "HasCoverGen": True,
            "HasDamageDeal": False,
            "HasFortify": True,
            "HasScan": False,
            "HasRevive": True,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "vantage") :
        return {
            "SeasonReleased": 14,
            "LegendClass": "Recon",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": False
        }
    elif (lowerName == "catalyst") :
        return {
            "SeasonReleased": 15,
            "LegendClass": "Controller",
            "HasCoverGen": True,
            "HasDamageDeal": False,
            "HasFortify": True,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "ballistic") :
        return {
            "SeasonReleased": 17,
            "LegendClass": "Assault",
            "HasCoverGen": False,
            "HasDamageDeal": True,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "conduit") :
        return {
            "SeasonReleased": 19,
            "LegendClass": "Support",
            "HasCoverGen": True,
            "HasDamageDeal": False,
            "HasFortify": False,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": False,
            "HasTeamMovement": False
        }
    elif (lowerName == "alter") :
        return {
            "SeasonReleased": 21,
            "LegendClass": "Skirmmisher",
            "HasCoverGen": False,
            "HasDamageDeal": False,
            "HasFortify": True,
            "HasScan": False,
            "HasRevive": False,
            "HasMovement": True,
            "HasTeamMovement": True
        }
    else :
        return None
    


def ReadApexRow(apexRow, lateAdditions) :

    apexGame = []

    gameId = str(apexRow[0])
    gameNumber = int(apexRow[1])
    datePlayed = datetime.strptime(apexRow[2], "%m/%d/%Y").date()
    timePlayed = datetime.strptime(apexRow[3], "%H:%M").time()
    dateTimePlayed = datetime.combine(datePlayed, timePlayed)
    season = safeInt(apexRow[4])
    gameType = str(apexRow[5])
    map = str(apexRow[6])
    landingSite = str(apexRow[7])
    deathSite = str(apexRow[8])
    hotZoneOriginal = safeInt(apexRow[9])
    
    hotZone = "Pre-Collection"
    if (lateAdditions.get("hotZone") == True) :
        hotZone = "Landed Hot" if hotZoneOriginal == 1 else "Landed Cold"
        
    else :
        if (hotZoneOriginal != None) :
            lateAdditions["hotZone"] = True

    legendDict = GetCharacterDetail(str(apexRow[10]))
    legendSelectionNumber = safeInt(apexRow[11])
    secondLegendDict = GetCharacterDetail(str(apexRow[12]))
    thirdLegendDict = GetCharacterDetail(str(apexRow[13]))

    legendJumpmaster = safeInt(apexRow[15])
    jumpmaster = "Pre-Collection"
    if (lateAdditions.get("jumpmaster") == True) :
        if (legendJumpmaster == 1) :
            jumpmaster = "Jumpmaster"
        elif (legendJumpmaster > 1) :
            jumpmaster = "Squadmate JM"
        else :
            jumpmaster = "Unknown"
    
    else :
        if (legendJumpmaster != None) :
            lateAdditions["jumpmaster"] = True
    
    damageDealt = safeInt(apexRow[16])
    teammate1DamageDealt = safeInt(apexRow[17])
    teammate2DamageDealt = safeInt(apexRow[18])

    myRankDetail = GetRankDetail(apexRow[19], gameType)
    teammate1RankDetail = GetRankDetail(apexRow[20], gameType)
    teammate2RankDetail = GetRankDetail(apexRow[21], gameType)

    myRank = RetrievNullableKey(myRankDetail, "rank")
    teammate1Rank = RetrievNullableKey(teammate1RankDetail, "rank")
    teammate2Rank = RetrievNullableKey(teammate2RankDetail, "rank")

    myRankLevel = RetrievNullableKey(myRankDetail, "rankLevel")
    teammate1RankLevel = RetrievNullableKey(teammate1RankDetail, "rankLevel")
    teammate2RankLevel = RetrievNullableKey(teammate2RankDetail, "rankLevel")

    myRankBroad = RetrievNullableKey(myRankDetail, "rankBroad")
    teammate1RankBroad = RetrievNullableKey(teammate1RankDetail, "rankBroad")
    teammate2RankBroad = RetrievNullableKey(teammate2RankDetail, "rankBroad")

    higherLevelSpot = str(apexRow[22])
    rankedLobby = GetRankedLobby(gameType, myRank, teammate1Rank, teammate2Rank, higherLevelSpot)
    rankedLobbyBaseline = GetRankBaseline(rankedLobby)

    lowLevel = safeInt(apexRow[23])
    lowLevelTm = "Pre-Collection"
    if (lateAdditions.get("lowLevel") == True) :
        lowLevelTm = "Low Level TM" if lowLevelTm == 1 else "No Low Level"
        
    else :
        if (lowLevel != None) :
            lateAdditions["lowLevel"] = True

    tm1RankedBadgeOriginal = str(apexRow[24])
    tm2RankedBadgeOriginal = str(apexRow[25])
    tm1RankedBadge = "Pre-Collection"
    tm2RankedBadge = "Pre-Collection"
    if (lateAdditions.get("tmRankedBadge") == True) :
        tm1RankedBadge = tm1RankedBadgeOriginal
        tm2RankedBadge = tm2RankedBadgeOriginal 
        
    else :
        if (tm1RankedBadgeOriginal != '' or 
            tm2RankedBadgeOriginal != '') :
            lateAdditions["tmRankedBadge"] = True

    tm1KillsBadgeOriginal = safeInt(apexRow[26])
    tm2KillsBadgeOriginal = safeInt(apexRow[27])
    tm1KillsBadge = "Pre-Collection"
    tm2KillsBadge = "Pre-Collection"
    if (lateAdditions.get("tmKillsBadge") == True) :
        tm1KillsBadge = str(apexRow[26])
        tm2KillsBadge = str(apexRow[27])
        
    else :
        if (tm1KillsBadgeOriginal != None or 
            tm2KillsBadgeOriginal != None) :
            lateAdditions["tmKillsBadge"] = True

    survivalTime = datetime.strptime(apexRow[28], "%H:%M").time()
    tm1SurvivalTime = datetime.strptime(apexRow[29], "%H:%M").time()
    tm2SurvivalTime = datetime.strptime(apexRow[30], "%H:%M").time()

    survivalTimeSecs = timeToSeconds(survivalTime)
    tm1SurvivalTimeSecs = timeToSeconds(tm1SurvivalTime)
    tm2SurvivalTimeSecs = timeToSeconds(tm2SurvivalTime)

    kills = safeInt(apexRow[31])
    tm1Kills = safeInt(apexRow[32])
    tm2Kills = safeInt(apexRow[33])
    knockdowns = safeInt(apexRow[34])

    firstLegendDeath = str(apexRow[35])
    secondLegendDeath = str(apexRow[36])
    thirdLegendDeath = str(apexRow[37])

    squadPlaced = safeInt(apexRow[38])

    reviveGiven = safeInt(apexRow[39])
    tm1ReviveGiven = safeInt(apexRow[40])
    tm2ReviveGiven = safeInt(apexRow[41])
    respawnGiven = safeInt(apexRow[42])
    tm1RespawnGiven = safeInt(apexRow[43])
    tm2RespawnGiven = safeInt(apexRow[44])

    tm1Console = str(apexRow[45])
    tm2Console = str(apexRow[46])

    diedInitialPhase = str(apexRow[47])

    apexGame.append(gameId)
    apexGame.append(gameNumber)
    apexGame.append(datePlayed)
    apexGame.append(timePlayed)
    apexGame.append(dateTimePlayed)
    apexGame.append(season)
    apexGame.append(gameType)
    apexGame.append(map)
    apexGame.append(landingSite)
    apexGame.append(deathSite)
    apexGame.append(hotZoneOriginal)
    apexGame.append(hotZone)
    apexGame.append(legendDict)
    apexGame.append(legendSelectionNumber)
    apexGame.append(secondLegendDict)
    apexGame.append(thirdLegendDict)
    apexGame.append(legendJumpmaster)
    apexGame.append(jumpmaster)
    apexGame.append(damageDealt)
    apexGame.append(teammate1DamageDealt)
    apexGame.append(teammate2DamageDealt)
    apexGame.append(myRank)
    apexGame.append(teammate1Rank)
    apexGame.append(teammate2Rank)
    apexGame.append(myRankLevel)
    apexGame.append(teammate1RankLevel)
    apexGame.append(teammate2RankLevel)
    apexGame.append(myRankBroad)
    apexGame.append(teammate1RankBroad)
    apexGame.append(teammate2RankBroad)
    apexGame.append(higherLevelSpot)
    apexGame.append(rankedLobby)
    apexGame.append(rankedLobbyBaseline)
    apexGame.append(lowLevel)
    apexGame.append(lowLevelTm)
    apexGame.append(tm1RankedBadgeOriginal)
    apexGame.append(tm1RankedBadge)
    apexGame.append(tm2RankedBadgeOriginal)
    apexGame.append(tm2RankedBadge)
    apexGame.append(tm1KillsBadgeOriginal)
    apexGame.append(tm1KillsBadge)
    apexGame.append(tm2KillsBadgeOriginal)
    apexGame.append(tm2KillsBadge)
    apexGame.append(survivalTime)
    apexGame.append(tm1SurvivalTime)
    apexGame.append(tm2SurvivalTime)
    apexGame.append(survivalTimeSecs)
    apexGame.append(tm1SurvivalTimeSecs)
    apexGame.append(tm2SurvivalTimeSecs)
    apexGame.append(kills)
    apexGame.append(tm1Kills)
    apexGame.append(tm2Kills)
    apexGame.append(knockdowns)
    apexGame.append(firstLegendDeath)
    apexGame.append(secondLegendDeath)
    apexGame.append(thirdLegendDeath)
    apexGame.append(squadPlaced)
    apexGame.append(reviveGiven)
    apexGame.append(tm1ReviveGiven)
    apexGame.append(tm2ReviveGiven)
    apexGame.append(respawnGiven)
    apexGame.append(tm1RespawnGiven)
    apexGame.append(tm2RespawnGiven)
    apexGame.append(diedInitialPhase)
    apexGame.append(tm1Console)
    apexGame.append(tm2Console)

    return apexGame

    
def safeInt(string) :
    try :
        return int(string)
    except: 
        return None
    
def RetrievNullableKey(dict, key) :
    if (dict == None) :
        return None
    else :
        return dict.get(key)


def GetRankDetail(rank, gameType):

    gameTypeLower = gameType.lower()
    if (gameTypeLower != "ranked") :
        return None

    if (rank == None) :
        return GetRankDictionary("Unknown", None, "Unknown")
    
    rankLower = str(rank).lower()
    rankClean = FirstLetterUpper(rank)

    if (rankLower == '' or
        rankLower == 'unknown') :
        return GetRankDictionary("Unknown", None, "Unknown")
    
    elif (rankLower == 'master') :
        return GetRankDictionary(rankClean, 26, "Master")
    
    elif (rankLower == 'predator') :
        return GetRankDictionary(rankClean, 27, "Predator")
    
    else :
        rankSpace = rank.find(" ")
        if (rankSpace == -1) :
            return GetRankDictionary("Unknown", None, "Unknown")
        
        rankBroad = rankClean[0:rankSpace]
        nestedRankLevel = safeInt(rankClean[(rankSpace + 1): len(rankClean)])
        if (nestedRankLevel == None) :
            return GetRankDictionary("Unknown", None, "Unknown")
        
        if (rankBroad == "Plat") :
            rankBaseline = GetRankBaseline("Platinum")
            rankLevel = rankBaseline + (4 - nestedRankLevel)
            return GetRankDictionary(rankClean, rankLevel, "Platinum")
        
        else :
            rankBaseline = GetRankBaseline(rankBroad)
            if (rankBaseline == None) :
                return GetRankDictionary("Unknown", None, "Unknown")

            rankLevel = rankBaseline + (4 - nestedRankLevel)
            return GetRankDictionary(rankClean, rankLevel, rankBroad)

         
def GetRankDictionary(rankName, rankLevel, rankBroadName) :

    if (rankName == None or
        rankName == '' or
        rankBroadName == None or 
        rankBroadName == '') :    
        return None

    return {
        "rank": rankName,
        "rankLevel": rankLevel,
        "rankBroad": rankBroadName,
    }

def GetRankBaseline(rankBroad) :
    
    if (rankBroad == None or 
        rankBroad == '') :   
        return None

    rankBroadLower = rankBroad.lower()
    if (rankBroadLower == 'unknown') :
        return None
    
    if (rankBroadLower == 'rookie') :
        return 1
    elif (rankBroadLower == 'bronze') :
        return 5
    elif (rankBroadLower == 'silver') :
        return 9
    elif (rankBroadLower == 'gold') :
        return 13
    elif (rankBroadLower == 'platinum') :
        return 17
    elif (rankBroadLower == 'diamond') :
        return 21
    elif (rankBroadLower == 'master' or rankBroadLower == 'predator') :
        return 25
    else :
        return None


def FirstLetterUpper(string):
    newString = ''
    charNumb = 0
    for char in string :
        curChar = char
        if (charNumb == 0) :
            curChar = char.upper()
        else :
            curChar = char.lower()
        
        charNumb += 1
        newString += curChar
    
    return newString


def GetRankedLobby(gameType, myRank, tm1Rank, tm2Rank, higherLevelSpot) :

    gameTypeLower = gameType.lower()
    if (gameTypeLower != "ranked") :
        return 'Non-Ranked'

    if (higherLevelSpot != None and
        higherLevelSpot != '') :
        
        if (higherLevelSpot == 'Master & Pred') :
            return "Master"
        
        else :
            return FirstLetterUpper(higherLevelSpot)
    
    myRankDict = GetRankDetail(myRank, gameType)
    tm1RankDict = GetRankDetail(tm1Rank, gameType)
    tm2RankDict = GetRankDetail(tm2Rank, gameType)

    myRankScore = RetrievNullableKey(myRankDict, "rankLevel")
    tm1RankScore = RetrievNullableKey(tm1RankDict, "rankLevel")
    tm2RankScore = RetrievNullableKey(tm2RankDict, "rankLevel")

    myRankBroad = FirstLetterUpper(RetrievNullableKey(myRankDict, "rankBroad"))
    tm1RankBroad = FirstLetterUpper(RetrievNullableKey(tm1RankDict, "rankBroad"))
    tm2RankBroad = FirstLetterUpper(RetrievNullableKey(tm2RankDict, "rankBroad"))

    if (myRankScore == None) :
        return 'Unknown'
    
    if (tm1RankScore == None or tm2RankScore == None) :
        return myRankBroad
    
    maxScore = max(myRankScore, tm1RankScore, tm2RankScore)

    if (maxScore == myRankScore) :
        return myRankBroad
    elif (maxScore == tm1RankScore) :
        return tm1RankBroad
    elif (maxScore == tm2RankBroad) :
        return tm2RankBroad
    else :
        return 'Unknown'
    
def timeToSeconds(t) :
    if (t == None) :
        return None
    
    return (t.hour * 3600) + (t.minute * 60) + (t.second)


def ReadCsv(fileName, keepHeaders) :
    dataset = open(fileName, "r", encoding="utf-8-sig")
    reader = csv.reader(dataset)
    data = []
    for i, row in enumerate(reader):
        if (not keepHeaders) :
            if (i == 0) :
                continue
                
        data.append(row)
    
    dataset.close()
    return data

def GetWeaponDictionary():
    weaponSeason = ReadCsv("WeaponSeason.csv", False)
    season_dict = {}

    for ws in weaponSeason:
        s = int(ws[0])
        
        if season_dict.get(f"{s}") == None:
            season_dict[f"{s}"] = {}

        season_dict[f"{s}"][f"{ws[1]}"] = {
            "weaponName": ws[1],
            "weaponType": ws[2],
            "ammoType": ws[3]
        }
    
    return season_dict


##def BuildRankBroadDictionary(rankName, rankBaseline) :

apexData = ReadApexData("ApexLegendsData.csv", 6000)
print(" ")
print(apexData[5000])

"""
apexCsv = open(fileName, "r", encoding="utf-8-sig")
reader = csv.reader(apexCsv)
for i, row in enumerate(reader):
    if (i > 10) :
        break
    print(row)
"""





















    

