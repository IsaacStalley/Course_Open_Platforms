#!/usr/bin/python3
"""
Created on Mon June 5 4:19:04 2020
@author: Isaac Stalley

Name_Fix program with a simple interface that takes a user name input,
checks the validity of the name and then fixes the upper and lower case
format of the name.
"""


# List used to store the corrected names
names = []


# nameFix function, receives a name and after checking the validity with
# the nameCheck function, fixes the format of the name and stores it.
def nameFix(name):
    name = name.strip()
    if nameCheck(name):
        name = name[0].upper() + name[1:].lower()
        i = 0
        while i < len(name):
            if name[i] == " ":
                name = name[:i+1] + name[i+1].upper() + name[i+2:]
            i += 1
        names.append(name)


# nameCheck function, checks if the name contains any non-alphameric
# characters as well as the permitted 3 to 4 names.
def nameCheck(name):
    space = 0
    for i in name:
        if i.isspace():
            space += 1
        elif i.isalpha() is False:
            return False
    if space < 2 or space > 3:
        return False
    return True


# Interface function, takes the user input and calls the nameFix function,
# also stops the program whenever the user desires.
def interface():
    while True:
        usrInput = input("Insert the name you wish to process or"
                         " SALIR if you wish to exit the program:")
        if usrInput != "SALIR":
            nameFix(usrInput)
        else:
            for i in names:
                print(i)
            break


# Runs the program by starting the interface function.
interface()
