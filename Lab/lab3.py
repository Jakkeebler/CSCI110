"""
Lab 3
updated by: Jeron Kuxhausen
CSCI 110
Date: Feb 2nd, 2016

Playing with functions and variables scope.
"""

#FIXME - Assign your name to myName variable
myName = "Jeron Kuxhausen"
# myName is a global variable

# Function that prints Hello World.
# Doesn't take any arguments and doesn't return a value
def printHello():
    print("Hello World!")

# Function that prints Hello World twice
# Simply Calls printHello function twice
def printHelloTwice():
    printHello()
    printHello()

# Function that takes one string, argument name and greets by name
def greetName(name):
    print("Hi there,", name)

# Function that greets someone
# Doesn't take any argument and doesn't return any value
def meetAndGreet():
    firstName = input("\nHey there! What's your name?\n")
    # firstName is a local variable
    # Call greet function to greet user
    greetName(firstName)
    print("My name is %s. Pleased to meet you!"%(myName))
    print()

# Function to print converted time
def printTime(seconds, seconds2, minutes, hours, days, weeks):
    print("You entered %d seconds."%(seconds))
    if seconds < 60:
        print("Your time is: %d seconds."%(seconds2))
    elif minutes >= 1 and hours < 1:
        print("Your time is: %d minutes, and %d seconds."%(minutes, seconds2))
    elif hours >= 1 and days < 1:
        print("Your time is: %d hours, %d minutes, and %d seconds."%(hours, minutes, seconds2))
    elif days >= 1 and weeks < 1:
        print("Your time is: %d days, %d hours, %d minutes, and %d seconds."%(days, hours, minutes, seconds2))
    elif weeks >= 1:
        print("Your time is: %d weeks, %d days, %d hours, %d minutes, and %d seconds."%(weeks, days, hours, minutes, seconds2))

#FIXME
# Define a function named convertTime that takes 1 integer argument called seconds.
# The function convers and print the seconds in hours, minutes, and seconds.
def convertTime():
    seconds = int(input("Please enter a time in seconds:\n"))

    minutes = 0
    hours = 0
    days = 0
    weeks = 0
    seconds2 = 0

    if seconds >= 60:
        minutes = int((seconds / 60))
        seconds2 = int((seconds % 60))

        if minutes >= 60:
            hours = int((minutes / 60) - .05)
            minutes = int((minutes - (60 * hours)))

            if hours >= 24:
                days = int(hours / 24)
                hours = int((hours - (24 * days)))

                if days >= 7:
                    weeks = int(days / 7)
                    days = int((days - (7 * weeks)))

    printTime(seconds, seconds2, minutes, hours, days, weeks)

# Call printHello function
printHello()

#FIXME - Call printHelloTwice function
printHelloTwice()

someName = "Bill Gates"
# Calling function passing variable as argument.
greetName(someName)
# Calling function passing literal valus as argument.
greetName("Larry Page")

#Call meetAndGreet
meetAndGreet()

#FIXME - Call function convertTime passing proper arguments
while True:
    convertTime()

    print("")
    ans = input("Would you like to enter another time? (y/n): \n")
    if ans != 'y':
        break