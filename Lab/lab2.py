"""
Lab 2
Updated by: Jeron Kuxhausen
Date: Jan 26, 2016
CSCI 110

This program calculates and displays the area and circumference of a circle with a radius of 5 units.

Algorithm Steps:
    1. Store radius into a variable.
    2. Calculate area using the formula (pi*radius*radius) and then store the value into a var.
    3. Calculate circumferance using formula (2*pi*radus) and store the value into a var.
    4. Display the calculated values of area and circumference.
"""
#Start Loop
while True:
    #Declare variables
    pi = 3.14159
    radius = float(input("Please enter a radius for your circle: \n"))

    #Calculations
    area = pi * radius **2
    circumference = pi * radius * 2

    #Print Values
    print("")
    print ("{:^30}".format("The properties of your circle"))
    print ("{:=<30}".format(""))
    print ("{:<8} {:<6} {:<15}".format("Radius", "Area", "Circumference"))
    print ("{:<8.2f} {:<6.2f} {:<15.2f}".format(radius, area, circumference))
    print ("{:=<30}".format(""))

    print("")
    ans = input("Would you like to enter another radius (y/n): \n")
    if ans != 'y':
        break

print("")
print("Thank you for using our app! Have a nice day!")
input("Press enter to close the application...\n")