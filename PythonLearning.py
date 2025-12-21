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

    weaponDict = GetWeaponDictionary()
    try :
        for i, row in enumerate(reader):
            if (numberRecs != None and i > (numberRecs + 1)):
                break

            if (i > 1) :
                apexGame = ReadApexRow(row, lateAdditions, weaponDict)
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
            "LegendName": "Bangalore",
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
            "LegendName": "Bloodhound",
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
            "LegendName": "Caustic",
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
            "LegendName": "Gibraltar",
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
            "LegendName": "Lifeline",
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
            "LegendName": "Mirage",
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
            "LegendName": "Pathfinder",
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
            "LegendName": "Wraith",
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
            "LegendName": "Octane",
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
            "LegendName": "Wattson",
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
            "LegendName": "Crypto",
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
            "LegendName": "Revenant",
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
            "LegendName": "Loba",
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
            "LegendName": "Rampart",
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
            "LegendName": "Horizon",
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
            "LegendName": "Fuse",
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
            "LegendName": "alkyrie",
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
            "LegendName": "Seer",
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
            "LegendName": "Ash",
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
            "LegendName": "Maggie",
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
            "LegendName": "Newcastle",
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
            "LegendName": "Vantage",
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
            "LegendName": "Catalyst",
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
            "LegendName": "Ballistic",
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
            "LegendName": "Conduit",
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
            "LegendName": "Alter",
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
    


def ReadApexRow(apexRow, lateAdditions, weaponDict) :

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

    originalPrimaryWeapon = str(apexRow[48])
    originalSecondaryWeapon = str(apexRow[49])
    weaponSeason = RetrievNullableKey(weaponDict, str(season))
    primaryWeaponDetail = RetrievNullableKey(weaponSeason, f"{originalPrimaryWeapon}")
    primaryWeapon = RetrievNullableKey(primaryWeaponDetail, "weaponName")
    primaryWeaponType =RetrievNullableKey(primaryWeaponDetail, "weaponType")
    primaryAmmoType = RetrievNullableKey(primaryWeaponDetail, "ammoType")

    secondaryWeaponDetail = RetrievNullableKey(weaponSeason, f"{originalSecondaryWeapon}")
    secondaryWeapon = RetrievNullableKey(secondaryWeaponDetail, "weaponName")
    secondaryWeaponType = RetrievNullableKey(secondaryWeaponDetail, "weaponType")
    secondaryAmmoType = RetrievNullableKey(secondaryWeaponDetail, "ammoType")

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
    apexGame.append(tm1RankedBadge)
    apexGame.append(tm2RankedBadge)
    apexGame.append(tm1KillsBadgeOriginal)
    apexGame.append(tm2KillsBadgeOriginal)
    apexGame.append(tm1KillsBadge)
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
    apexGame.append(primaryWeapon)
    apexGame.append(primaryWeaponType)
    apexGame.append(primaryAmmoType)
    apexGame.append(secondaryWeapon)
    apexGame.append(secondaryWeaponType)
    apexGame.append(secondaryAmmoType)

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

def TranformApexData(apexGames) :
    cleanApexGames = []
    apexGames = sorted(apexGames, key=lambda game: game[4])
    sessionNumber = 1

    #Previous Game Logic
    rollingGames = []
    previousDateTime = None

    for apexGame in apexGames :      
        fullGameData = []
        curGameId = apexGame[0]
        curGameNumber = apexGame[1]
        curDatePlayedString = datetime.strptime(apexGame[2], '%Y/%m/%d')
        
        curHourPlayed = apexGame[3].hour
        curTimePeriodPlayed = ''
        if (curHourPlayed <= 5) :
            curTimePeriodPlayed = 'Evening'
        elif (curHourPlayed <= 11) :
            curTimePeriodPlayed = 'Morning'
        elif (curHourPlayed <= 17) :
            curTimePeriodPlayed = 'Afternoon'
        elif (curHourPlayed <= 23) :
            curTimePeriodPlayed = 'Evening'
        else :
            curTimePeriodPlayed = 'Unknown'

        curTimePlayedString = datetime.strptime(apexGame[3], '%H:%M')
        curDateTime = apexGame[4]

        if (previousDateTime != None and 
            (curDateTime - previousDateTime).total_seconds() > (60 * 60 * 4)) :
            sessionNumber += 1
        
        previousDateTime = curDateTime

        curSeason = apexGame[5]
        gameType = apexGame[6]
        if (gameType != 'Ranked' and
            gameType != 'Trios') :
            gameType = 'Special GM'
        
        map = apexGame[7]
        landingSite = apexGame[8]
        deathSite = apexGame[9]
        if (deathSite == '') :
            deathSite = 'No Death'

        landedHotBinary = apexGame[10]
        landedHot = apexGame[11]

        legendDict = apexGame[12]
        legendSelectionNumber = apexGame[13]
        secondLegendDict = apexGame[14]
        thirdLegendDict = apexGame[15]

        #Legend Selected
        legendNewThreshold = 2

        legendSelected = RetrievNullableKey(legendDict, "LegendName")
        legendSeason = RetrievNullableKey(legendDict, "SeasonReleased")
        legendNew = GetLegendNewOld(curSeason, legendSeason, legendNewThreshold)
        legendOg = GetOgLegend(legendSeason)
        legendClass = RetrievNullableKey(legendDict, "LegendClass")
        
        legendHasCoverGen = RetrievNullableKey(legendDict, "HasCoverGen")
        legendCoverGen = GetAbilityCoverage(legendHasCoverGen, "Cover-Gen")

        legendHasDamageDeal = RetrievNullableKey(legendDict, "HasDamageDeal")
        legendDamageDeal = GetAbilityCoverage(legendHasDamageDeal, "Damage Dealing")

        legendHasFortify = RetrievNullableKey(legendDict, "HasFortify")
        legendFortify = GetAbilityCoverage(legendHasFortify, "Fortify")

        legendHasScan = RetrievNullableKey(legendDict, "HasScan")
        legendScan = GetAbilityCoverage(legendHasScan, "Scan")

        legendHasRevive = RetrievNullableKey(legendDict, "HasRevive")
        legendRevive = GetAbilityCoverage(legendHasRevive, "Revive")

        legendHasMovement = RetrievNullableKey(legendDict, "HasMovement")
        legendMovement = GetAbilityCoverage(legendHasMovement, "Movement")

        legendHasTeamMovement = RetrievNullableKey(legendDict, "HasTeamMovement")
        legendTeamMovement = GetAbilityCoverage(legendHasTeamMovement, "Team Movement")

        legendSelectedFavourite = GetFavouriteLegend(legendSelected)

        #Second Legend Selected
        secondLegendSelected = RetrievNullableKey(secondLegendDict, "LegendName")
        secondLegendSeason = RetrievNullableKey(secondLegendDict, "SeasonReleased")
        secondLegendNew = GetLegendNewOld(curSeason, secondLegendSeason, legendNewThreshold)
        secondLegendOg = GetOgLegend(secondLegendSeason)
        secondLegendClass = RetrievNullableKey(secondLegendDict, "LegendClass")
        
        secondLegendHasCoverGen = RetrievNullableKey(secondLegendDict, "HasCoverGen")
        secondLegendCoverGen = GetAbilityCoverage(secondLegendHasCoverGen, "Cover-Gen")

        secondLegendHasDamageDeal = RetrievNullableKey(secondLegendDict, "HasDamageDeal")
        secondLegendDamageDeal = GetAbilityCoverage(secondLegendHasDamageDeal, "Damage Dealing")

        secondLegendHasFortify = RetrievNullableKey(secondLegendDict, "HasFortify")
        secondLegendFortify = GetAbilityCoverage(secondLegendHasFortify, "Fortify")

        secondLegendHasScan = RetrievNullableKey(secondLegendDict, "HasScan")
        secondLegendScan = GetAbilityCoverage(secondLegendHasScan, "Scan")

        secondLegendHasRevive = RetrievNullableKey(secondLegendDict, "HasRevive")
        secondLegendRevive = GetAbilityCoverage(secondLegendHasRevive, "Revive")

        secondLegendHasMovement = RetrievNullableKey(secondLegendDict, "HasMovement")
        secondLegendMovement = GetAbilityCoverage(secondLegendHasMovement, "Movement")

        secondLegendHasTeamMovement = RetrievNullableKey(secondLegendDict, "HasTeamMovement")
        secondLegendTeamMovement = GetAbilityCoverage(secondLegendHasTeamMovement, "Team Movement")


        #Third Legend Selected
        thirdLegendSelected = RetrievNullableKey(thirdLegendDict, "LegendName")
        thirdLegendSeason = RetrievNullableKey(thirdLegendDict, "SeasonReleased")
        thirdLegendNew = GetLegendNewOld(curSeason, thirdLegendSeason, legendNewThreshold)
        thirdLegendOg = GetOgLegend(secondLegendSeason)
        thirdLegendClass = RetrievNullableKey(thirdLegendDict, "LegendClass")
        
        thirdLegendHasCoverGen = RetrievNullableKey(thirdLegendDict, "HasCoverGen")
        thirdLegendCoverGen = GetAbilityCoverage(thirdLegendHasCoverGen, "Cover-Gen")

        thirdLegendHasDamageDeal = RetrievNullableKey(thirdLegendDict, "HasDamageDeal")
        thirdLegendDamageDeal = GetAbilityCoverage(thirdLegendHasDamageDeal, "Damage Dealing")

        thirdLegendHasFortify = RetrievNullableKey(thirdLegendDict, "HasFortify")
        thirdLegendFortify = GetAbilityCoverage(thirdLegendHasFortify, "Fortify")

        thirdLegendHasScan = RetrievNullableKey(thirdLegendDict, "HasScan")
        thirdLegendScan = GetAbilityCoverage(thirdLegendHasScan, "Scan")

        thirdLegendHasRevive = RetrievNullableKey(thirdLegendDict, "HasRevive")
        thirdLegendRevive = GetAbilityCoverage(thirdLegendHasRevive, "Revive")

        thirdLegendHasMovement = RetrievNullableKey(thirdLegendDict, "HasMovement")
        thirdLegendMovement = GetAbilityCoverage(thirdLegendHasMovement, "Movement")

        thirdLegendHasTeamMovement = RetrievNullableKey(thirdLegendDict, "HasTeamMovement")
        thirdLegendTeamMovement = GetAbilityCoverage(thirdLegendHasTeamMovement, "Team Movement")

        squadNewLegend = GetSquadNewLegend(curSeason, 
                                           legendSeason, secondLegendSeason, thirdLegendSeason, 
                                           legendNewThreshold)
        
        squadOgLegend = GetSquadOgLegend(legendSeason, secondLegendSeason, thirdLegendSeason)

        squadCoverGen = SquadAbilityCoverage(
            legendHasCoverGen, secondLegendHasCoverGen, thirdLegendHasCoverGen, "Cover-Gen")

        squadDamageDealing = SquadAbilityCoverage(
            legendHasDamageDeal, secondLegendHasDamageDeal, thirdLegendHasDamageDeal, "Damage")
        
        squadFortify = SquadAbilityCoverage(
            legendHasFortify, secondLegendHasFortify, thirdLegendHasFortify, "Fortify")
        
        squadRevive = SquadAbilityCoverage(
            legendHasRevive, secondLegendHasRevive, thirdLegendHasRevive, "Revive")
        
        squadScan = SquadAbilityCoverage(
            legendHasScan, secondLegendHasScan, thirdLegendHasScan, "Scan")
        
        squadTeamMovement = SquadAbilityCoverage(
            legendHasTeamMovement, secondLegendHasTeamMovement, thirdLegendHasTeamMovement, "Team Movement")

        jumpmasterLegend = apexGame[16]
        jumpmaster = apexGame[17]

        damageDealt = apexGame[18]
        tm1DamageDealt = apexGame[19]
        tm2DamageDealt = apexGame[20]

        squadDamageDealt = damageDealt + tm1DamageDealt + tm2DamageDealt

        damageDealtBandsSmall = BandNumericField(damageDealt, 50, 3000)
        tm1DamageDealtBandsSmall = BandNumericField(tm1DamageDealt, 50, 3000)
        tm2DamageDealtBandsSmall = BandNumericField(tm2DamageDealt, 50, 3000)

        damageDealtBands = BandNumericField(damageDealt, 100, 3000)
        tm1DamageDealtBands = BandNumericField(tm1DamageDealt, 100, 3000)
        tm2DamageDealtBands = BandNumericField(tm2DamageDealt, 100, 3000)

        damageDealtBandsLarge = BandNumericField(damageDealt, 250, 3000)
        tm1DamageDealtBandsLarge = BandNumericField(tm1DamageDealt, 250, 3000)
        tm2DamageDealtBandsLarge = BandNumericField(tm2DamageDealt, 250, 3000)

        damageVsTm1 = damageDealt - tm1DamageDealt
        damageVsTm2 = damageDealt - tm2DamageDealt
        damageVsTeammates = damageVsTm1 + damageVsTm2

        damagePositionSquad = 0
        damagePositionCategory = ''
        totalTmsExceededDamage = 0
        if (damageDealt >= tm1DamageDealt and damageDealt >= tm2DamageDealt) :
            damagePositionSquad = 1
            damagePositionCategory = '1st'
            totalTmsExceededDamage = 2
        elif (damageDealt >= tm1DamageDealt or damageDealt >= tm2DamageDealt) :
            damagePositionSquad = 2
            damagePositionCategory = '2nd'
            totalTmsExceededDamage = 1
        else :
            damagePositionSquad = 3
            damagePositionCategory = '3rd'
            totalTmsExceededDamage = 0  

        damageProportionBanded = BandNumericField(SafeDivide(damageDealt, squadDamageDealt) * 100, 10, 1000)

        myRank = apexGame[21]
        tm1Rank = apexGame[22]
        tm2Rank = apexGame[23]

        myRankScore = apexGame[24]
        tm1RankScore = apexGame[25]
        tm2RankScore = apexGame[26]

        myRankBroad = apexGame[27]
        tm1RankBroad = apexGame[28]
        tm2RankBroad = apexGame[29]

        rankedLobby = apexGame[31]
        rankedBaseline = apexGame[32]

        lowerRankTm = ""
        if (gameType != "Ranked") :
            lowerRankTm = "Non-Ranked"
        else :
            if (tm1RankScore >= rankedBaseline and
                tm2RankScore >= rankedBaseline) :
                lowerRankTm = "Correct Rank TMs"
            elif (tm1RankScore < rankedBaseline or
                  tm2RankScore < rankedBaseline) :
                lowerRankTm = "Lower Rank TM"
            else :
                lowerRankTm = "Unknown"


        lowLevelTm = apexGame[34]

        tm1RankedBadge = apexGame[35]
        tm2RankedBadge = apexGame[36]
        
        tm1KillsBadge = apexGame[39]
        tm2KillsBadge = apexGame[40]

        tm1KillsBadgeBanded = BandNumericField(apexGame[37], 500, 6000)
        tm2KillsBadgeBanded = BandNumericField(apexGame[38], 500, 6000)

        survivalTime = apexGame[41].strftime("%H:%M")
        survivalTimeSecs = apexGame[44]
        survivalTimeMins = math.floor(survivalTimeSecs / 60)
        survivalTimeMinsCapped = BandNumericField(survivalTimeMins, 1, 15)
        survivalTimeMinsBanded = BandNumericField(survivalTimeMins, 3, 15)

        tm1SurvivalTime = apexGame[42].strftime("%H:%M")
        tm1SurvivalTimeSecs = apexGame[45]
        tm1SurvivalTimeMins = math.floor(tm1SurvivalTimeSecs / 60)
        tm1SurvivalTimeMinsCapped = BandNumericField(tm1SurvivalTimeMins, 1, 15)
        tm1SurvivalTimeMinsBanded = BandNumericField(tm1SurvivalTimeMins, 3, 15)

        tm2SurvivalTime = apexGame[43].strftime("%H:%M")
        tm2SurvivalTimeSecs = apexGame[46]
        tm2SurvivalTimeMins = math.floor(tm2SurvivalTimeSecs / 60)
        tm2SurvivalTimeMinsCapped = BandNumericField(tm2SurvivalTimeMins, 1, 15)
        tm2SurvivalTimeMinsBanded = BandNumericField(tm2SurvivalTimeMins, 3, 15)

        kills = apexGame[47]
        tm1Kills = apexGame[48]
        tm2Kills = apexGame[49]

        killsBanded = BandNumericField(kills, 1, 7)
        tm1KillsBanded = BandNumericField(tm1Kills, 1, 7)
        tm2KillsBanded = BandNumericField(tm2Kills, 1, 7)

        knockdowns = apexGame[50]
        knockdownsBanded = BandNumericField(knockdowns, 1, 7)

        squadKills = kills + tm1Kills + tm2Kills

        firstLegendDeath = apexGame[51]
        secondLegendDeath = apexGame[52]
        thirdLegendDeath = apexGame[53]

        squadDeathPosition = ''
        if (firstLegendDeath == legendSelected) :
            squadDeathPosition = '1st'
        elif (secondLegendDeath == legendSelected) :
            squadDeathPosition = '2nd'
        elif (thirdLegendDeath == legendSelected) :
            squadDeathPosition = '3rd'

        squadPlacement = apexGame[54]
        squadPlacementString = StringifyNumericPosition(squadPlacement)
        
        reviveGiven = apexGame[55]
        tm1ReviveGiven = apexGame[56]
        tm2ReviveGiven = apexGame[57]
        squadReviveGiven = reviveGiven + tm1ReviveGiven + tm2ReviveGiven

        respawnGiven = apexGame[58]
        tm1RespawnGiven = apexGame[59]
        tm2RespawnGiven = apexGame[60]
        squadRespawnGiven = respawnGiven + tm1RespawnGiven + tm2RespawnGiven

        squadResRev = squadReviveGiven + squadRespawnGiven

        diedInitialPhase = apexGame[61]
        tm1Console = apexGame[62]
        tm2Console = apexGame[63]

        primaryWeapon = apexGame[64]
        primaryWeaponType = apexGame[65]
        primaryWeaponAmmo = apexGame[66]

        secondaryWeapon = apexGame[67]
        secondaryWeaponType = apexGame[68]
        secondaryWeaponAmmo = apexGame[69]

        for historicGame in rollingGames :
            print("Hello")

        for historicGame in rollingGames :
            print("Hello")
        
        fullGameData.append(curGameId)
        fullGameData.append(curGameNumber)
        fullGameData.append(curDatePlayedString)
        fullGameData.append(curTimePlayedString)
        fullGameData.append(curHourPlayed)
        fullGameData.append(sessionNumber)
        fullGameData.append(curSeason)
        fullGameData.append(gameType)
        fullGameData.append(map)
        fullGameData.append(landingSite)
        fullGameData.append(deathSite)
        fullGameData.append(landedHotBinary)
        fullGameData.append(landedHot)
        fullGameData.append(jumpmasterLegend)
        fullGameData.append(jumpmaster)
        fullGameData.append(legendSelected)
        fullGameData.append(legendSeason)
        fullGameData.append(legendNew)
        fullGameData.append(legendOg)
        fullGameData.append(legendClass)
        fullGameData.append(legendCoverGen)
        fullGameData.append(legendDamageDeal)
        fullGameData.append(legendFortify) 
        fullGameData.append(legendRevive)
        fullGameData.append(legendScan)
        fullGameData.append(legendMovement)
        fullGameData.append(legendTeamMovement)
        fullGameData.append(legendSelectedFavourite)
        fullGameData.append(legendSelectionNumber)
        fullGameData.append(secondLegendSelected)
        fullGameData.append(secondLegendClass)
        fullGameData.append(secondLegendSeason)
        fullGameData.append(secondLegendNew)
        fullGameData.append(secondLegendOg)
        fullGameData.append(secondLegendCoverGen)
        fullGameData.append(secondLegendDamageDeal)
        fullGameData.append(secondLegendFortify)
        fullGameData.append(secondLegendRevive)
        fullGameData.append(secondLegendScan)
        fullGameData.append(secondLegendMovement)
        fullGameData.append(secondLegendTeamMovement)
        fullGameData.append(thirdLegendSelected)
        fullGameData.append(thirdLegendClass)
        fullGameData.append(thirdLegendSeason)
        fullGameData.append(thirdLegendNew)
        fullGameData.append(thirdLegendOg)
        fullGameData.append(thirdLegendCoverGen)
        fullGameData.append(thirdLegendDamageDeal)
        fullGameData.append(thirdLegendFortify)
        fullGameData.append(thirdLegendRevive)
        fullGameData.append(thirdLegendScan)
        fullGameData.append(thirdLegendMovement)
        fullGameData.append(thirdLegendTeamMovement)
        fullGameData.append(squadNewLegend)
        fullGameData.append(squadOgLegend)
        fullGameData.append(squadCoverGen)
        fullGameData.append(squadDamageDealing)
        fullGameData.append(squadFortify)
        fullGameData.append(squadRevive)
        fullGameData.append(squadScan)
        fullGameData.append(squadTeamMovement)
        fullGameData.append(jumpmasterLegend)
        fullGameData.append(jumpmaster)
        fullGameData.append(damageDealt)
        fullGameData.append(tm1DamageDealt)
        fullGameData.append(tm2DamageDealt)
        fullGameData.append(squadDamageDealt)
        fullGameData.append(damageDealtBandsSmall)
        fullGameData.append(tm1DamageDealtBandsSmall)
        fullGameData.append(tm2DamageDealtBandsSmall)
        fullGameData.append(damageDealtBands)
        fullGameData.append(tm1DamageDealtBands)
        fullGameData.append(tm2DamageDealtBands)
        fullGameData.append(damageDealtBandsLarge)
        fullGameData.append(tm1DamageDealtBandsLarge)
        fullGameData.append(tm2DamageDealtBandsLarge)
        fullGameData.append(damageVsTm1)
        fullGameData.append(damageVsTm2)
        fullGameData.append(damageVsTeammates)
        fullGameData.append(damagePositionSquad)
        fullGameData.append(damagePositionCategory)
        fullGameData.append(totalTmsExceededDamage)
        fullGameData.append(damageProportionBanded)
        fullGameData.append(myRank)
        fullGameData.append(tm1Rank)
        fullGameData.append(tm2Rank)
        fullGameData.append(myRankScore)
        fullGameData.append(tm1RankScore)
        fullGameData.append(tm2RankScore)
        fullGameData.append(myRankBroad)
        fullGameData.append(tm1RankBroad)
        fullGameData.append(tm2RankBroad)
        fullGameData.append(rankedLobby)
        fullGameData.append(rankedBaseline)
        fullGameData.append(lowerRankTm)
        fullGameData.append(lowLevelTm)
        fullGameData.append(tm1RankedBadge)
        fullGameData.append(tm2RankedBadge)
        fullGameData.append(tm1KillsBadge)
        fullGameData.append(tm2KillsBadge)
        fullGameData.append(tm1KillsBadgeBanded)
        fullGameData.append(tm2KillsBadgeBanded)
        fullGameData.append(survivalTime)
        fullGameData.append(survivalTimeSecs)
        fullGameData.append(survivalTimeMins)
        fullGameData.append(survivalTimeMinsCapped)
        fullGameData.append(survivalTimeMinsBanded)
        fullGameData.append(tm1SurvivalTime)
        fullGameData.append(tm1SurvivalTimeSecs)
        fullGameData.append(tm1SurvivalTimeMins)
        fullGameData.append(tm1SurvivalTimeMinsCapped)
        fullGameData.append(tm1SurvivalTimeMinsBanded)
        fullGameData.append(tm2SurvivalTime)
        fullGameData.append(tm2SurvivalTimeSecs)
        fullGameData.append(tm2SurvivalTimeMins)
        fullGameData.append(tm2SurvivalTimeMinsCapped)
        fullGameData.append(tm2SurvivalTimeMinsBanded)
        fullGameData.append(kills)
        fullGameData.append(tm1Kills)
        fullGameData.append(tm2Kills)
        fullGameData.append(killsBanded)
        fullGameData.append(tm1KillsBanded)
        fullGameData.append(tm2KillsBanded)
        fullGameData.append(knockdowns)
        fullGameData.append(knockdownsBanded)
        fullGameData.append(squadKills)
        fullGameData.append(firstLegendDeath)
        fullGameData.append(secondLegendDeath)
        fullGameData.append(thirdLegendDeath)
        fullGameData.append(squadDeathPosition)
        fullGameData.append(squadPlacement)
        fullGameData.append(squadPlacementString)
        fullGameData.append(reviveGiven)
        fullGameData.append(tm1ReviveGiven)
        fullGameData.append(tm2ReviveGiven)
        fullGameData.append(squadReviveGiven)
        fullGameData.append(respawnGiven)
        fullGameData.append(tm1RespawnGiven)
        fullGameData.append(tm2RespawnGiven)
        fullGameData.append(squadRespawnGiven)
        fullGameData.append(squadResRev)
        fullGameData.append(diedInitialPhase)
        fullGameData.append(tm1Console)
        fullGameData.append(tm2Console)
        fullGameData.append(primaryWeapon)
        fullGameData.append(primaryWeaponAmmo)
        fullGameData.append(primaryWeaponType)
        fullGameData.append(secondaryWeapon)
        fullGameData.append(secondaryWeaponAmmo)
        fullGameData.append(secondaryWeaponType)



def GetLegendNewOld(season, legendSeason, newThreshold) :
    if ((season - legendSeason) <= newThreshold) :
        return "New Legend"
    else :
        return "Old Legend"

def GetSquadNewLegend(season, legendSeason, tm1LegendSeason, tm2LegendSeason, newThreshold) :
    if ((season - legendSeason) <= newThreshold or 
        (season - tm1LegendSeason) <= newThreshold or 
        (season - tm2LegendSeason) <= newThreshold) :
        return "New Legend Squad"
    else :
        return "No New Legend Squad"
    
def GetOgLegend(legendSeason) :
    if (legendSeason == 0) :
        return "OG-Legend"
    else :
        return "Non OG-Legend"
    
def GetSquadOgLegend(legendSeason, tm1LegendSeason, tm2LegendSeason) :
    if (legendSeason == 0 or
        tm1LegendSeason == 0 or
        tm2LegendSeason == 0) :
        return "Squad OG-Legend"
    else :
        return "No OG-Legend"

def GetFavouriteLegend(legendSelected) :
    legendLower = legendSelected.lower()
    if (legendLower == "bangalore") :
        return "Favourite Legend"
    else :
        return "Non Favourite Legend"


def GetAbilityCoverage(hasAbility, abilityName) :
    if (hasAbility) :
        return f"Has {abilityName}"
    else :
        return f"No {abilityName}"


def SquadAbilityCoverage(playerAbility, tm1Ability, tm2Ability, abilityName) :
    if (playerAbility or 
        tm1Ability or 
        tm2Ability) :
        return f"Squad Has {abilityName}"
    else :
        return f"Squad No {abilityName}"


def BandNumericField(number, bandSize, cap) :
    safeNumber = safeInt(number)
    if (safeNumber == None) :
        return ''

    if (safeNumber >= cap) :
        return f"{cap}+"
    
    floored = math.floor(safeNumber / bandSize) * bandSize
    banded = f"${floored} - {floored + bandSize - 1}"
    return banded


def SafeDivide(numerator, denominator) :
    if (denominator == 0) :
        return 0
    else :
        return (numerator / denominator)


def StringifyNumericPosition(numericPosition) :   
    numericSafe = safeInt(numericPosition)
    if (numericSafe == None) :
        return ''

    if (numericPosition == 1) :
        return '1st'
    elif (numericPosition == 2) :
        return '2nd'
    elif (numericPosition ==3) :
        return '3rd'
    else :
        return f"{numericPosition}th"


##def BuildRankBroadDictionary(rankName, rankBaseline) :

apexData = ReadApexData("ApexLegendsData.csv", 6000)
print(" ")
print(apexData[5460])

"""
apexCsv = open(fileName, "r", encoding="utf-8-sig")
reader = csv.reader(apexCsv)
for i, row in enumerate(reader):
    if (i > 10) :
        break
    print(row)
"""











