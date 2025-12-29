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

def ReadApexData(fileName, numberRecs = None): 
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

            if (i > 0) :
                apexGame = ReadApexRow(row, lateAdditions, weaponDict)
                apexData.append(apexGame)
                rowCount += 1
    except Exception as e:
        print(f"There was an error retrieving the data: {e}")
           
    print(f"Successfully retrieved {rowCount} records from the Apex Dataset")
    apexCsv.close()
    cleanApexData = []
   
    try :
        cleanApexData = TransformApexData(apexData)
    except Exception as e:
        print(f"There was an error transforming the data: {e}")

    return cleanApexData

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

    survivalTimeSecs = (timeToSeconds(survivalTime) / 60)
    tm1SurvivalTimeSecs = (timeToSeconds(tm1SurvivalTime) / 60)
    tm2SurvivalTimeSecs = (timeToSeconds(tm2SurvivalTime) / 60)

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
        clean_string = str(string).replace(",", "").strip()
        return int(clean_string)
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

def TransformApexData(apexGames) :
    cleanApexGames = []
    apexGames = sorted(apexGames, key=lambda game: game[4])
    sessionNumber = 1
    sessionId = 'SID-1'

    #Previous Game Logic
    rollingGames = []
    previousDateTime = None
    firstDateTime = apexGames[0][4]

    for apexGame in apexGames :      
        fullGameData = []
        curGameId = apexGame[0]
        curGameNumber = apexGame[1]
        curDatePlayedString = apexGame[2].strftime('%Y/%m/%d')
        
        curHourPlayed = apexGame[3].hour
        timePeriodPlayed = ''
        if (curHourPlayed <= 4) :
            timePeriodPlayed = 'Evening'
        elif (curHourPlayed <= 11) :
            timePeriodPlayed = 'Morning'
        elif (curHourPlayed <= 17) :
            timePeriodPlayed = 'Afternoon'
        elif (curHourPlayed > 17) :
            timePeriodPlayed = 'Evening'  
        else :
            timePeriodPlayed = 'Unknown'          


        curTimePlayedString = apexGame[3].strftime('%H:%M')
        curDateTime = apexGame[4]
        curDateTimeString = curDateTime.strftime("%Y/%m/%d %H:%M")

        if (previousDateTime != None and 
            (curDateTime - previousDateTime).total_seconds() > (60 * 60 * 4)) :
            sessionNumber += 1
            sessionId = f"SID-{sessionNumber}"
        
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
            if (rankedBaseline == None) :
                lowerRankTm = "Unknown"
            elif (tm1RankScore == None or tm2RankScore == None) :
                lowerRankTm = "Unknown"
            elif (tm1RankScore >= rankedBaseline and
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

        previous14DaysTotalGames = 0
        previous14DaysTotalTime = 0

        previous14DaysTotalPlacement = 0
        previous14DaysAvgPlacement = 0
        previous14DaysTop1s = 0
        previous14DaysTop3s = 0
        previous14DaysTop5s = 0

        previous14DaysDamageDealt = 0
        previous14Days600Dmg = 0
        previous14Days900Dmg = 0
        previous14Days1200Dmg = 0

        previous14DaysKnockdowns = 0
        previous14Days1Knockdowns = 0
        previous14Days2Knockdowns = 0
        previous14Days3Knockdowns = 0

        previous14DaysKills = 0
        previous14Days1Kills = 0
        previous14Days2Kills = 0
        previous14Days3Kills = 0

        previous30DaysTotalGames = 0
        previous30DaysTotalTime = 0

        gameNumberSession = 1
        previousGameTimeSession = 0
        
        previousPlacement = 0
        previous1Top1 = 0
        previous1Top3 = 0
        previous1Top5 = 0

        previousDamageDealt = 0
        previous1600Dmg = 0
        previous1900Dmg = 0
        previous11200Dmg = 0

        previousKnockdowns = 0
        previous11Knockdowns = 0
        previous12Knockdowns = 0
        previous13Knockdowns = 0

        previousKills = 0
        previous11Kills = 0
        previous12Kills = 0
        previous13Kills = 0
        
        previous3Placement = 0
        previous3AvgPlacement = 0
        previous3Top1 = 0
        previous3Top3 = 0
        previous3Top5 = 0

        previous3DamageDealt = 0
        previous3600Dmg = 0
        previous3900Dmg = 0
        previous31200Dmg = 0
       
        previous3Kills = 0
        previous31Kills = 0
        previous32Kills = 0
        previous33Kills = 0

        previous3Knockdowns = 0
        previous31Knockdowns = 0
        previous32Knockdowns = 0
        previous33Knockdowns = 0

        previous5Placement = 0
        previous5AvgPlacement = 0
        previous5Top1 = 0
        previous5Top3 = 0
        previous5Top5 = 0

        previous5DamageDealt = 0
        previous5600Dmg = 0
        previous5900Dmg = 0
        previous51200Dmg = 0
       
        previous5Kills = 0
        previous51Kills = 0
        previous52Kills = 0
        previous53Kills = 0
        
        previous5Knockdowns = 0
        previous51Knockdowns = 0
        previous52Knockdowns = 0
        previous53Knockdowns = 0

        # If the game number is 1 the logic will never be reached via historic games (none exist).
        if (curGameNumber == 1) :

                previous14DaysTotalGames = ''
                previous14DaysTotalTime = ''

                previous14DaysAvgPlacement = ''
                previous14DaysTop1s = ''
                previous14DaysTop3s = ''
                previous14DaysTop5s = ''
                previous14DaysDamageDealt = ''
                previous14Days600Dmg = ''
                previous14Days900Dmg = ''
                previous14Days1200Dmg = ''
                previous14DaysKills = ''
                previous14Days1Kills = ''
                previous14Days2Kills = ''
                previous14Days3Kills = ''
                previous14DaysKnockdowns = ''
                previous14Days1Knockdowns = ''
                previous14Days2Knockdowns = ''
                previous14Days3Knockdowns = ''    

                previous30DaysTotalGames = ''   
                previous30DaysTotalTime = ''   

                previousPlacement = '' 
                previous1Top1 = ''
                previous1Top3 = ''
                previous1Top5 = ''
                previous3AvgPlacement = ''
                previous3Top1 = ''
                previous3Top3 = ''
                previous3Top5 = ''
                previous5AvgPlacement = ''
                previous5Top1 = ''
                previous5Top3 = ''
                previous5Top5 = ''

                previousDamageDealt = ''
                previous1600Dmg = ''
                previous1900Dmg = ''
                previous11200Dmg = ''
                previous3DamageDealt = ''
                previous3600Dmg = ''
                previous3900Dmg = ''
                previous31200Dmg = ''
                previous5DamageDealt = ''
                previous5600Dmg = ''
                previous5900Dmg = ''
                previous51200Dmg = ''     

                previousKills = '' 
                previous11Kills = ''     
                previous12Kills = ''      
                previous13Kills = ''           
                previous3Kills = '' 
                previous31Kills = ''     
                previous32Kills = ''      
                previous33Kills = ''    
                previous5Kills = '' 
                previous51Kills = ''     
                previous52Kills = ''      
                previous53Kills = ''    

                previousKnockdowns = '' 
                previous11Knockdowns = ''     
                previous12Knockdowns = ''      
                previous13Knockdowns = ''           
                previous3Knockdowns = '' 
                previous31Knockdowns = ''     
                previous32Knockdowns = ''      
                previous33Knockdowns = ''    
                previous5Knockdowns = '' 
                previous51Knockdowns = ''     
                previous52Knockdowns = ''      
                previous53Knockdowns = ''   

        curDateTimePlayed = apexGame[4]
        rollingGames = FilterRollingGames(rollingGames, curGameNumber, sessionNumber, curDateTimePlayed)

        for historicGame in rollingGames :
            histGame = int(historicGame[1])
            histSession = int(historicGame[7])
            histDateTime = GetDateTime(historicGame[2], historicGame[3])

            histSurvivalSecs = int(historicGame[138])
            histSquadPlacement = int(historicGame[189])
            histDamageDealt = int(historicGame[86])
            histKills = int(historicGame[152])
            histKnockdowns = int(historicGame[171])
            
            firstGameWithin30Days = (curDateTimePlayed - firstDateTime).days <= 30
            firstGameWithin14Days = (curDateTimePlayed - firstDateTime).days <= 14
            within14Days = (curDateTimePlayed - histDateTime).days <= 14
            within30Days = (curDateTimePlayed - histDateTime).days <= 30
            within5Games = (curGameNumber <= (histGame + 5) and curGameNumber > histGame)
            within3Games = (curGameNumber <= (histGame + 3) and curGameNumber > histGame)
            within1Games = (curGameNumber <= (histGame + 1) and curGameNumber > histGame)
            sameSession = (sessionNumber == histSession)

            #Same Session
            if (sameSession) :
                gameNumberSession += 1
                previousGameTimeSession += histSurvivalSecs

            #14 Days
            if (firstGameWithin14Days) :

                previous14DaysTotalGames = ''
                previous14DaysTotalTime = ''

                previous14DaysAvgPlacement = ''
                previous14DaysTop1s = ''
                previous14DaysTop3s = ''
                previous14DaysTop5s = ''
                previous14DaysDamageDealt = ''
                previous14Days600Dmg = ''
                previous14Days900Dmg = ''
                previous14Days1200Dmg = ''
                previous14DaysKills = ''
                previous14Days1Kills = ''
                previous14Days2Kills = ''
                previous14Days3Kills = ''
                previous14DaysKnockdowns = ''
                previous14Days1Knockdowns = ''
                previous14Days2Knockdowns = ''
                previous14Days3Knockdowns = ''
            
            else :
                if (within14Days) :
                    previous14DaysTotalGames += 1
                    previous14DaysTotalTime += histSurvivalSecs
                    
                    previous14DaysTotalPlacement += histSquadPlacement
                    previous14DaysAvgPlacement = math.floor(SafeDivide(previous14DaysTotalPlacement, previous14DaysTotalGames))
                    
                    if (histSquadPlacement <= 5) :
                        previous14DaysTop5s += 1
                        if (histSquadPlacement <= 3) :
                            previous14DaysTop3s += 1
                            if (histSquadPlacement <= 1) :
                                previous14DaysTop1s += 1
                    
                    previous14DaysDamageDealt += histDamageDealt
                    if (histDamageDealt >= 600) :
                        previous14Days600Dmg += 1
                        if (histDamageDealt >= 900) :
                            previous14Days900Dmg += 1
                            if (histDamageDealt >= 1200) :
                                previous14Days1200Dmg += 1

                    previous14DaysKills += histKills
                    if (histKills >= 1) :
                        previous14Days1Kills += 1
                        if (histKills >= 2) :
                            previous14Days2Kills += 1
                            if (histKills >= 3) :
                                previous14Days3Kills += 1

                    previous14DaysKnockdowns += histKnockdowns
                    if (histKnockdowns >= 1) :
                        previous14Days1Knockdowns += 1
                        if (histKnockdowns >= 2) :
                            previous14Days2Knockdowns += 1
                            if (histKnockdowns >= 3) :
                                previous14Days3Knockdowns += 1

            # 30 Days
            if (firstGameWithin30Days) :
                previous30DaysTotalGames = ''
                previous30DaysTotalTime = ''

            else :
                if (within30Days) :
                    previous30DaysTotalGames += 1
                    previous30DaysTotalTime += histSurvivalSecs

            # Previous 1 Games
            if (curGameNumber <= 1) :
                previousPlacement = ''
                previous1Top5 = ''
                previous1Top3 = ''
                previous1Top3 = ''

                previousDamageDealt = ''
                previous1600Dmg = ''
                previous1900Dmg = ''
                previous11200Dmg = ''

                previousKills = ''
                previous11Kills = ''
                previous12Kills = ''
                previous13Kills = ''

                previousKnockdowns = ''
                previous11Knockdowns = ''
                previous12Knockdowns = ''
                previous13Knockdowns = ''

            else :
                if (within1Games) : 
                    previousPlacement = histSquadPlacement
                    if (histSquadPlacement <= 5) :
                        previous1Top5 += 1
                        if (histSquadPlacement <= 3) :
                            previous1Top3 += 1
                            if (histSquadPlacement <= 1) :
                                previous1Top1 += 1

                    previousDamageDealt = histDamageDealt
                    if (histDamageDealt >= 600) :
                        previous1600Dmg += 1
                        if (histDamageDealt >= 900) :
                            previous1900Dmg += 1
                            if (histDamageDealt >= 1200)  :
                                previous11200Dmg += 1

                    previousKills = histKills
                    if (histKills >= 1) :
                        previous11Kills += 1
                        if (histKills >= 2) :
                            previous12Kills += 1
                            if (histKills >= 3) :
                                previous13Kills += 1

                    previousKnockdowns = histKnockdowns
                    if (histKnockdowns >= 1) :
                        previous11Knockdowns += 1
                        if (histKnockdowns >= 2) :
                            previous12Knockdowns += 1
                            if (histKnockdowns >= 3) :
                                previous13Knockdowns += 1                

            if (curGameNumber <= 3) :
                previous3AvgPlacement = ''
                previous3Top5 = ''
                previous3Top3 = ''
                previous3Top3 = ''

                previous3DamageDealt = ''
                previous3600Dmg = ''
                previous3900Dmg = ''
                previous31200Dmg = ''

                previous3Kills = ''
                previous31Kills = ''
                previous32Kills = ''
                previous33Kills = ''

                previous3Knockdowns = ''
                previous31Knockdowns = ''
                previous32Knockdowns = ''
                previous33Knockdowns = ''

            else :
                if (within3Games) : 
                    previous3Placement += histSquadPlacement
                    previous3AvgPlacement = math.floor(previous3Placement / 3)
                    if (histSquadPlacement <= 5) :
                        previous3Top5 += 1
                        if (histSquadPlacement <= 3) :
                            previous3Top3 += 1
                            if (histSquadPlacement <= 1) :
                                previous3Top1 += 1

                    previous3DamageDealt += histDamageDealt
                    if (histDamageDealt >= 600) :
                        previous3600Dmg += 1
                        if (histDamageDealt >= 900) :
                            previous3900Dmg += 1
                            if (histDamageDealt >= 1200)  :
                                previous31200Dmg += 1

                    previous3Kills += histKills
                    if (histKills >= 1) :
                        previous31Kills += 1
                        if (histKills >= 2) :
                            previous32Kills += 1
                            if (histKills >= 3) :
                                previous33Kills += 1

                    previous3Knockdowns += histKnockdowns
                    if (histKnockdowns >= 1) :
                        previous31Knockdowns += 1
                        if (histKnockdowns >= 2) :
                            previous32Knockdowns += 1
                            if (histKnockdowns >= 3) :
                                previous33Knockdowns += 1             

            if (curGameNumber <= 5) :
                previous5AvgPlacement = ''
                previous5Top5 = ''
                previous5Top3 = ''
                previous5Top3 = ''

                previous5DamageDealt = ''
                previous5600Dmg = ''
                previous5900Dmg = ''
                previous51200Dmg = ''

                previous5Kills = ''
                previous51Kills = ''
                previous52Kills = ''
                previous53Kills = ''

                previous5Knockdowns = ''
                previous51Knockdowns = ''
                previous52Knockdowns = ''
                previous53Knockdowns = ''

            else :
                if (within5Games) : 
                    previous5Placement += histSquadPlacement
                    previous5AvgPlacement = math.floor(previous5Placement / 5)
                    if (histSquadPlacement <= 5) :
                        previous5Top5 += 1
                        if (histSquadPlacement <= 3) :
                            previous5Top3 += 1
                            if (histSquadPlacement <= 1) :
                                previous5Top1 += 1

                    previous5DamageDealt += histDamageDealt
                    if (histDamageDealt >= 600) :
                        previous5600Dmg += 1
                        if (histDamageDealt >= 900) :
                            previous5900Dmg += 1
                            if (histDamageDealt >= 1200)  :
                                previous51200Dmg += 1

                    previous5Kills += histKills
                    if (histKills >= 1) :
                        previous51Kills += 1
                        if (histKills >= 2) :
                            previous52Kills += 1
                            if (histKills >= 3) :
                                previous53Kills += 1

                    previous5Knockdowns += histKnockdowns
                    if (histKnockdowns >= 1) :
                        previous51Knockdowns += 1
                        if (histKnockdowns >= 2) :
                            previous52Knockdowns += 1
                            if (histKnockdowns >= 3) :
                                previous53Knockdowns += 1     
        
        fullGameData.append(curGameId) #1
        fullGameData.append(curGameNumber) #2
        fullGameData.append(curDatePlayedString) #3
        fullGameData.append(curTimePlayedString) #4
        fullGameData.append(curDateTimeString) #5
        fullGameData.append(curHourPlayed) #6
        fullGameData.append(timePeriodPlayed) #7
        fullGameData.append(sessionNumber) #8
        fullGameData.append(sessionId) #9
        fullGameData.append(gameNumberSession) #10
        fullGameData.append(previousGameTimeSession) #11
        fullGameData.append(previous14DaysTotalGames) #12
        fullGameData.append(previous14DaysTotalTime) #13
        fullGameData.append(previous14DaysAvgPlacement) #14
        fullGameData.append(previous14DaysTop1s) #15
        fullGameData.append(previous14DaysTop3s) #16
        fullGameData.append(previous14DaysTop5s) #17
        fullGameData.append(previous14DaysDamageDealt) #18
        fullGameData.append(previous14Days600Dmg) #19
        fullGameData.append(previous14Days900Dmg) #20
        fullGameData.append(previous14Days1200Dmg) #21
        fullGameData.append(previous14DaysKills) #22
        fullGameData.append(previous14Days1Kills) #23
        fullGameData.append(previous14Days2Kills) #24
        fullGameData.append(previous14Days3Kills) #25
        fullGameData.append(previous14DaysKnockdowns) #26
        fullGameData.append(previous14Days1Knockdowns) #27
        fullGameData.append(previous14Days2Knockdowns) #28
        fullGameData.append(previous14Days3Knockdowns) #29
        fullGameData.append(previous30DaysTotalGames) #30
        fullGameData.append(previous30DaysTotalTime) #31
        fullGameData.append(curSeason) #32
        fullGameData.append(gameType) #33
        fullGameData.append(map) #34
        fullGameData.append(landingSite) #35
        fullGameData.append(deathSite) #36
        fullGameData.append(landedHotBinary) #37
        fullGameData.append(landedHot) #38
        fullGameData.append(jumpmasterLegend) #39
        fullGameData.append(jumpmaster) #40
        fullGameData.append(legendSelected) #41
        fullGameData.append(legendClass) #42
        fullGameData.append(legendSeason) #43
        fullGameData.append(legendNew) #44
        fullGameData.append(legendOg) #45
        fullGameData.append(legendCoverGen) #46
        fullGameData.append(legendDamageDeal) #47
        fullGameData.append(legendFortify) #48
        fullGameData.append(legendRevive) #49
        fullGameData.append(legendScan) #50
        fullGameData.append(legendMovement) #51
        fullGameData.append(legendTeamMovement) #52
        fullGameData.append(legendSelectedFavourite) #53
        fullGameData.append(legendSelectionNumber) #54
        fullGameData.append(secondLegendSelected) #55
        fullGameData.append(secondLegendClass) #56
        fullGameData.append(secondLegendSeason) #57
        fullGameData.append(secondLegendNew) #58
        fullGameData.append(secondLegendOg) #59
        fullGameData.append(secondLegendCoverGen) #60
        fullGameData.append(secondLegendDamageDeal) #61
        fullGameData.append(secondLegendFortify) #62
        fullGameData.append(secondLegendRevive) #63
        fullGameData.append(secondLegendScan) #64
        fullGameData.append(secondLegendMovement) #65
        fullGameData.append(secondLegendTeamMovement) #66
        fullGameData.append(thirdLegendSelected) #67
        fullGameData.append(thirdLegendClass) #68
        fullGameData.append(thirdLegendSeason) #69
        fullGameData.append(thirdLegendNew) #70
        fullGameData.append(thirdLegendOg) #71
        fullGameData.append(thirdLegendCoverGen) #72
        fullGameData.append(thirdLegendDamageDeal) #73
        fullGameData.append(thirdLegendFortify) #74
        fullGameData.append(thirdLegendRevive) #75
        fullGameData.append(thirdLegendScan) #76
        fullGameData.append(thirdLegendMovement) #77
        fullGameData.append(thirdLegendTeamMovement) #78
        fullGameData.append(squadNewLegend) #79
        fullGameData.append(squadOgLegend) #80
        fullGameData.append(squadCoverGen) #81
        fullGameData.append(squadDamageDealing) #82
        fullGameData.append(squadFortify) #83
        fullGameData.append(squadRevive) #84
        fullGameData.append(squadScan) #85
        fullGameData.append(squadTeamMovement) #86
        fullGameData.append(damageDealt) #87
        fullGameData.append(tm1DamageDealt) #88
        fullGameData.append(tm2DamageDealt) #89
        fullGameData.append(squadDamageDealt) #90
        fullGameData.append(damageDealtBandsSmall) #91
        fullGameData.append(tm1DamageDealtBandsSmall) #92
        fullGameData.append(tm2DamageDealtBandsSmall) #93
        fullGameData.append(damageDealtBands) #94
        fullGameData.append(tm1DamageDealtBands) #95
        fullGameData.append(tm2DamageDealtBands) #96
        fullGameData.append(damageDealtBandsLarge) #97
        fullGameData.append(tm1DamageDealtBandsLarge) #98
        fullGameData.append(tm2DamageDealtBandsLarge) #99
        fullGameData.append(damageVsTm1) #100
        fullGameData.append(damageVsTm2) #101
        fullGameData.append(damageVsTeammates) #102
        fullGameData.append(damagePositionSquad) #103
        fullGameData.append(damagePositionCategory) #104
        fullGameData.append(totalTmsExceededDamage) #105
        fullGameData.append(damageProportionBanded) #106
        fullGameData.append(previousDamageDealt) #107
        fullGameData.append(previous1600Dmg) #108
        fullGameData.append(previous1900Dmg) #109
        fullGameData.append(previous11200Dmg) #110
        fullGameData.append(previous3DamageDealt) #111
        fullGameData.append(previous3600Dmg) #112
        fullGameData.append(previous3900Dmg) #113
        fullGameData.append(previous31200Dmg) #114
        fullGameData.append(previous5DamageDealt) #115
        fullGameData.append(previous5600Dmg) #116
        fullGameData.append(previous5900Dmg) #117
        fullGameData.append(previous51200Dmg) #118
        fullGameData.append(myRank) #119
        fullGameData.append(tm1Rank) #120
        fullGameData.append(tm2Rank) #121
        fullGameData.append(myRankScore) #122
        fullGameData.append(tm1RankScore) #123
        fullGameData.append(tm2RankScore) #124
        fullGameData.append(myRankBroad) #125
        fullGameData.append(tm1RankBroad) #126
        fullGameData.append(tm2RankBroad) #127
        fullGameData.append(rankedLobby) #128
        fullGameData.append(rankedBaseline) #129
        fullGameData.append(lowerRankTm) #130
        fullGameData.append(lowLevelTm) #131
        fullGameData.append(tm1RankedBadge) #132
        fullGameData.append(tm2RankedBadge) #133
        fullGameData.append(tm1KillsBadge) #134
        fullGameData.append(tm2KillsBadge) #135
        fullGameData.append(tm1KillsBadgeBanded) #136
        fullGameData.append(tm2KillsBadgeBanded) #137
        fullGameData.append(survivalTime) #138
        fullGameData.append(survivalTimeSecs) #139
        fullGameData.append(survivalTimeMins) #140
        fullGameData.append(survivalTimeMinsCapped) #141
        fullGameData.append(survivalTimeMinsBanded) #142
        fullGameData.append(tm1SurvivalTime) #143
        fullGameData.append(tm1SurvivalTimeSecs) #144
        fullGameData.append(tm1SurvivalTimeMins) #145
        fullGameData.append(tm1SurvivalTimeMinsCapped) #146
        fullGameData.append(tm1SurvivalTimeMinsBanded) #147
        fullGameData.append(tm2SurvivalTime) #148
        fullGameData.append(tm2SurvivalTimeSecs) #149
        fullGameData.append(tm2SurvivalTimeMins) #150
        fullGameData.append(tm2SurvivalTimeMinsCapped) #151
        fullGameData.append(tm2SurvivalTimeMinsBanded) #152
        fullGameData.append(kills) #153
        fullGameData.append(tm1Kills) #154
        fullGameData.append(tm2Kills) #155
        fullGameData.append(squadKills) #156
        fullGameData.append(killsBanded) #157
        fullGameData.append(tm1KillsBanded) #158
        fullGameData.append(tm2KillsBanded) #159
        fullGameData.append(previousKills) #160
        fullGameData.append(previous11Kills) #161
        fullGameData.append(previous12Kills) #162
        fullGameData.append(previous13Kills) #163
        fullGameData.append(previous3Kills) #164
        fullGameData.append(previous31Kills) #165
        fullGameData.append(previous32Kills) #166
        fullGameData.append(previous33Kills) #167
        fullGameData.append(previous5Kills) #168
        fullGameData.append(previous51Kills) #169
        fullGameData.append(previous52Kills) #170
        fullGameData.append(previous53Kills) #171
        fullGameData.append(knockdowns) #172
        fullGameData.append(knockdownsBanded) #173
        fullGameData.append(previousKnockdowns) #174
        fullGameData.append(previous11Knockdowns) #175
        fullGameData.append(previous12Knockdowns) #176
        fullGameData.append(previous13Knockdowns) #177
        fullGameData.append(previous3Knockdowns) #178
        fullGameData.append(previous31Knockdowns) #179
        fullGameData.append(previous32Knockdowns) #180
        fullGameData.append(previous33Knockdowns) #181
        fullGameData.append(previous5Knockdowns) #182
        fullGameData.append(previous51Knockdowns) #183
        fullGameData.append(previous52Knockdowns) #184
        fullGameData.append(previous53Knockdowns) #185
        fullGameData.append(firstLegendDeath) #186
        fullGameData.append(secondLegendDeath) #187
        fullGameData.append(thirdLegendDeath) #188
        fullGameData.append(squadDeathPosition) #189
        fullGameData.append(squadPlacement) #190
        fullGameData.append(squadPlacementString) #191
        fullGameData.append(previousPlacement) #192
        fullGameData.append(previous1Top1) #193
        fullGameData.append(previous1Top3) #194
        fullGameData.append(previous1Top5) #195
        fullGameData.append(previous3AvgPlacement) #196
        fullGameData.append(previous3Top1) #197
        fullGameData.append(previous3Top3) #198
        fullGameData.append(previous3Top5) #199
        fullGameData.append(previous5AvgPlacement) #200
        fullGameData.append(previous5Top1) #201
        fullGameData.append(previous5Top3) #202
        fullGameData.append(previous5Top5) #203
        fullGameData.append(reviveGiven) #204
        fullGameData.append(tm1ReviveGiven) #205
        fullGameData.append(tm2ReviveGiven) #206
        fullGameData.append(squadReviveGiven) #207
        fullGameData.append(respawnGiven) #208
        fullGameData.append(tm1RespawnGiven) #209
        fullGameData.append(tm2RespawnGiven) #210
        fullGameData.append(squadRespawnGiven) #211
        fullGameData.append(squadResRev) #212
        fullGameData.append(diedInitialPhase) #213
        fullGameData.append(tm1Console) #214
        fullGameData.append(tm2Console) #215
        fullGameData.append(primaryWeapon) #216
        fullGameData.append(primaryWeaponAmmo) #217
        fullGameData.append(primaryWeaponType) #218
        fullGameData.append(secondaryWeapon) #219
        fullGameData.append(secondaryWeaponAmmo) #220
        fullGameData.append(secondaryWeaponType) #221

        #print(f"Game Number: {curGameNumber}")

        rollingGames.append(fullGameData)
        cleanApexGames.append(fullGameData)

    return cleanApexGames



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
        if (bandSize == 1) :
            return f"{cap}+"
        else :
            return f"'{cap}+"
    
    if (bandSize == 1) :
        return f"{number}"

    floored = math.floor(safeNumber / bandSize) * bandSize
    banded = f"'{floored} - {floored + bandSize - 1}"
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
    
def GetDateTime(dateStr, timeStr) :
    return datetime.strptime(
                f"{dateStr} {timeStr}",
                "%Y/%m/%d %H:%M"
            )

def FilterRollingGames(rollingGames, curGameNumber, curSessionNumber, curDateTimePlayed) :
    filteredGames = []
    for ag in rollingGames :
        
        try :
        
            gameNumber = int(ag[1])
            dateStr = ag[2]
            timeStr = ag[3]
            sessionNumber = int(ag[5])

            playedAt = GetDateTime(dateStr, timeStr)
            withinLast5Games = gameNumber >= (curGameNumber - 5)
            sameSession = sessionNumber == curSessionNumber
            within30Days = (curDateTimePlayed - playedAt).days <= 30

            if (withinLast5Games or 
                sameSession or
                within30Days) :
                filteredGames.append(ag)

        except Exception as e:
            print(f"Error translating filtered game: {e}")
            print(f"Offending record: {ag}")

    return filteredGames

def WriteCleanApexData(fileName, cleanData) :
    apexHeaders = GetCleanApexHeaders()
    cleanData.insert(0, apexHeaders)
    dataDump = open(f"{fileName}.csv", "w", newline="", encoding="utf-8")
    fileWriter = csv.writer(dataDump)
    fileWriter.writerows(cleanData)
    dataDump.close()


def GetCleanApexHeaders() :
    return [
        "Game_ID", 
        "Game_Number", 
        "Date_Played", 
        "Time_Played", 
        "DateTime_Played", 
        "Hour_Played", 
        "Time_Period_Played", 
        "Session_Number", 
        "Session_ID", 
        "Game_Number_Session", 
        "Time_Played_Session", 
        "Previous14_Total_Games", 
        "Previous14_Time_Played",
        "Previous14_Avg_Placement", 
        "Previous14_Top1s_Games", 
        "Previous14_Top3s_Games", 
        "Previous14_Top5s_Games", 
        "Previous14_DamageDealt", 
        "Previous14_600Dmg_Games", 
        "Previous14_900Dmg_Games", 
        "Previous14_1200Dmg_Games", 
        "Previous14_Kills", 
        "Previous14_1Kills_Games", 
        "Previous14_2Kills_Games", 
        "Previous14_3Kills_Games", 
        "Previous14_Knockdowns", 
        "Previous14_1Knockdowns_Games", 
        "Previous14_2Knockdowns_Games", 
        "Previous14_3Knockdowns_Games", 
        "Previous30_Total_Games", 
        "Previous30_Time_Played", 
        "Season", 
        "Gametype", 
        "Map", 
        "Landing_Site", 
        "Death_Site", 
        "Hot_Zone_Binary", 
        "Hot_Zone", 
        "Jumpmaster_Legend", 
        "Jumpmaster", 
        "Legend_Selected",
        "Legend_Class", 
        "Legend_Season", 
        "Legend_New", 
        "Legend_OG",  
        "Legend_CoverGen", 
        "Legend_DamageDeal", 
        "Legend_Fortify", 
        "Legend_Revive", 
        "Legend_Scan", 
        "Legend_Movement", 
        "Legend_TeamMovement", 
        "Legend_Selected_Favourite", 
        "Legend_Selection_Number", 
        "Second_Legend_Selected", 
        "Second_Legend_Class", 
        "Second_Legend_Season", 
        "Second_Legend_New", 
        "Second_Legend_OG", 
        "Second_Legend_CoverGen", 
        "Second_Legend_DamageDeal", 
        "Second_Legend_Fortify", 
        "Second_Legend_Revive", 
        "Second_Legend_Scan", 
        "Second_Legend_Movement", 
        "Second_Legend_TeamMovement", 
        "Third_Legend_Selected", 
        "Third_Legend_Class", 
        "Third_Legend_Season", 
        "Third_Legend_New", 
        "Third_Legend_OG", 
        "Third_Legend_CoverGen", 
        "Third_Legend_DamageDeal", 
        "Third_Legend_Fortify", 
        "Third_Legend_Revive", 
        "Third_Legend_Scan", 
        "Third_Legend_Movement", 
        "Third_Legend_TeamMovement", 
        "Squad_New_Legend", 
        "Squad_OG_Legend", 
        "Squad_CoverGen", 
        "Squad_DamageDeal", 
        "Squad_Fortify", 
        "Squad_Revive", 
        "Squad_Scan", 
        "Squad_TeamMovement", 
        "Damage_Dealt", 
        "TM1_Damage_Dealt", 
        "TM2_Damage_Dealt", 
        "Squad_Damage_Dealt", 
        "Damage_Dealt_Bands_Small", 
        "TM1_Damage_Dealt_Bands_Small", 
        "TM2_Damage_Dealt_Bands_Small", 
        "Damage_Dealt_Bands", 
        "TM1_Damage_Dealt_Bands", 
        "TM2_Damage_Dealt_Bands", 
        "Damage_Dealt_Bands_Large", 
        "TM1_Damage_Dealt_Bands_Large", 
        "TM2_Damage_Dealt_Bands_Large", 
        "Damage_Vs_TM1", 
        "Damage_Vs_TM2", 
        "Damge_Vs_Teammates", 
        "Damage_Position_Squad", 
        "Damage_Position_Category", 
        "Total_TMs_Exceeded_Damage", 
        "Damage_Proportion_Banded", 
        "Previous_Damage_Dealt", 
        "Previous_1_600Dmg", 
        "Previous_1_900Dmg", 
        "Previous_1_1200Dmg",
        "Previous_3_Damage_Dealt", 
        "Previous_3_600Dmg", 
        "Previous_3_900Dmg", 
        "Previous_3_1200Dmg", 
        "Previous_5_Damage_Dealt", 
        "Previous_5_600Dmg", 
        "Previous_5_900Dmg", 
        "Previous_5_1200Dmg", 
        "My_Rank", 
        "TM1_Rank", 
        "TM2_Rank", 
        "My_Rank_Score", 
        "TM1_Rank_Score", 
        "TM2_Rank_Score", 
        "My_Rank_Broad", 
        "TM1_Rank_Broad", 
        "TM2_Rank_Broad", 
        "Ranked_Lobby", 
        "Ranked_Baseline", 
        "Lower_Rank_TM", 
        "Low_Level_TM", 
        "TM1_Ranked_Badge", 
        "TM2_Ranked_Badge", 
        "TM1_Kills_Badge",
        "TM2_Kills_Badge", 
        "TM1_Kills_Badge_Banded", 
        "TM2_Kills_Badge_Banded", 
        "Survival_Time", 
        "Survival_Time_Secs", 
        "Survival_Time_Mins", 
        "Survival_Time_Mins_Capped", 
        "Survival_Time_Mins_Banded", 
        "TM1_Survival_Time", 
        "TM1_Survival_Time_Secs", 
        "TM1_Survival_Time_Mins", 
        "TM1_Survival_Time_Mins_Capped", 
        "TM1_Survival_Time_Mins_Banded", 
        "TM2_Survival_Time", 
        "TM2_Survival_Time_Secs", 
        "TM2_Survival_Time_Mins", 
        "TM2_Survival_Time_Mins_Capped", 
        "TM2_Survival_Time_Mins_Banded", 
        "Kills", 
        "TM1_Kills", 
        "TM2_Kills", 
        "Squad_Kills", 
        "Kills_Banded", 
        "TM1_Kills_Banded", 
        "TM2_Kills_Banded", 
        "Previous_Kills", 
        "Previous_1_1Kills", 
        "Previous_1_2Kills", 
        "Previous_1_3Kills", 
        "Previous_3_Kills",
        "Previous_3_1Kills",
        "Previous_3_2Kills",
        "Previous_3_3Kills",
        "Previous_5_Kills",
        "Previous_5_1Kills",
        "Previous_5_2Kills",
        "Previous_5_3Kills",
        "Knockdowns", 
        "Knockdowns_Banded", 
        "Previous_Knockdowns", 
        "Previous_1_1Knockdowns", 
        "Previous_1_2Knockdowns", 
        "Previous_1_3Knockdowns", 
        "Previous_3_Knockdowns", 
        "Previous_3_1Knockdowns", 
        "Previous_3_2Knockdowns", 
        "Previous_3_3Knockdowns", 
        "Previous_5_Knockdowns", 
        "Previous_5_1Knockdowns", 
        "Previous_5_2Knockdowns", 
        "Previous_5_3Knockdowns", 
        "First_Legend_Death", 
        "Second_Legend_Death", 
        "Third_Legend_Death", 
        "Squad_Death_Position", 
        "Squad_Placement", 
        "Squad_Placement_String", 
        "Previous_Placement", 
        "Previous_1_Top1s", 
        "Previous_1_Top3s", 
        "Previous_1_Top5s", 
        "Previous_3_AvgPlacement", 
        "Previous_3_Top1s", 
        "Previous_3_Top3s", 
        "Previous_3_Top5s", 
        "Previous_5_AvgPlacement", 
        "Previous_5_Top1s", 
        "Previous_5_Top3s", 
        "Previous_5_Top5s", 
        "Revive_Given", 
        "TM1_Revive_Given", 
        "TM2_Revive_Given", 
        "Squad_Revive_Given", 
        "Respawn_Given", 
        "TM1_Respawn_Given", 
        "TM2_Respawn_Given", 
        "Squad_Respawn_Given", 
        "Died_Initial_Phase", 
        "TM1_Console", 
        "TM2_Console", 
        "Primary_Weapon", 
        "Primary_Weapon_Ammo",
        "Primary_Weapon_Type", 
        "Secondary_Weapon", 
        "Secondary_Weapon_Ammo",
        "Secondary_Weapon_Type"
    ]

#Within 5 Games
#Within 30 Days
#Within Same Session

##def BuildRankBroadDictionary(rankName, rankBaseline) :

print(" ")
print("-------")
print("BEGINNING FINAL APEX LEGENDS PROJECT")
print("-------")
print(" ")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Preparing a clean Apex Legends dataset for analysis at: {now}.")
apexData = ReadApexData("ApexLegendsData.csv", 200)
print(" ")
try :
    print(f"Printing record 1000 of the data: {apexData[999]}.")
except:
    print("The row does not exist.")
WriteCleanApexData("CleanApexLegendsData", apexData)
print(" ")
print("Process finished.")

"""
apexCsv = open(fileName, "r", encoding="utf-8-sig")
reader = csv.reader(apexCsv)
for i, row in enumerate(reader):
    if (i > 10) :
        break
    print(row)
"""











