"""
Jeron Kuxhausen
Jan 29th, 2016
Homework 2
CSCI 110

Algorithm Steps
    1.Prompt user for Length and Width
    2.Store Length and Width in Variables
    3.Calculate perimeter.
    4.Calculate area.
    5.Output data for rectangle to console.
"""

print("Welcome to my rectangle program!")

#Start loop
while True:

    #User input of Length and Width
    length = float(input("Please enter a length for the rectangle:\n"))
    width = float(input("Please enter a width for the rectangle:\n"))

    #Calculations
    perimeter = (length + width) * 2
    area = length * width

    #Output
    print("")
    print("{:^33}".format("Your Rectangle Data"))
    print("{:=<33}".format(""))
    print("{:<8} {:<7} {:<6} {:<11}".format("Length", "Width", "Area", "Perimeter"))
    print("{:<8.2f} {:<7.2f} {:<6.2f} {:<11.2f}".format(length, width, area, perimeter))
    print("{:=<33}".format(""))

    print("")
    ans = input("Would you like to enter another radius (y/n): \n")
    if ans != 'y':
        break

print("")
print("Thank you for using our app! Have a nice day!")
input("Press enter to close the application...\n")