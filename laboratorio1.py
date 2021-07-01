#!/usr/bin/python3
"""
Created on Mon June 1 4:19:04 2020
@author: Isaac Stalley

Triangle program with a simple interface that takes a user input for the base
size of the triangle (middle row) as well as the character to use and prints
a triangle composed of the user's character.
"""


# Triangle function, prints a triangle using a char parameter for the character
# to print and a size parameter for the base size of the triangle (middle row).
def triangle(char, size):
    for i in range(1, size + 1):
        row = ""
        for x in range(i):
            row += char
        print(row)
    for i in range(size - 1, 0, -1):
        row = ""
        for x in range(i):
            row += char
        print(row)


# Interface function, takes the user inputs and calls the triangle function,
# also stops the program whenever the user desires.
def interface():
    while True:
        stop = input("Insert SALIR if you wish to exit the program or"
                     " anything else to continue...")
        if stop != "SALIR":
            char = input("Insert the character you wish to use:")
            size = int(input("Insert the size of the base you wish to use:"))
            triangle(char, size)
        else:
            break


# Runs the program by starting the interface function.
interface()
