#!/usr/bin/python3
"""
Created on Mon June 16 1:00:00 2020
@author: Isaac Stalley

Quadratic equation solver program, takes in variables
a,b,c through a txt file "entrada.txt" and saves the
results in a txt file "salida.txt".
"""
import math


# Function that checks and returns if the float is a whole
# number, else returns it rounded to the nearest 2 decimals.
def roundNumber(x):
    if x.is_integer():
        return int(x)
    else:
        return round(x, 2)


# Quadratic function, solves quadratic equations,
# returns the solutions else if the equation has infinite
# solutions or no solutions.
def quadratic(a, b, c):
    dis = b**2 - 4*a*c
    if (a, b, c) == (0, 0, 0):
        return "SOLUCIONES-INFINITAS"
    if dis < 0 or a == 0:
        return "SIN-SOLUCION"
    else:
        x1 = (-b + math.sqrt(dis)) / (2*a)
        x2 = (-b - math.sqrt(dis)) / (2*a)
        x1, x2 = (roundNumber(x1), roundNumber(x2))
        return str(x1) + "," + str(x2)


# Program that opens "entrada.txt" and uses the variables
# to solve quadratic equations calling the quadratic function
# and then saves the results in "salida.txt".
data = open("entrada.txt", "r")
results = open("salida.txt", "w+")
for i in data:
    line = i.split(',')
    result = quadratic(float(line[0]), float(line[1]), float(line[2]))
    results.write(result + "\n")
data.close()
results.close()
