#!/usr/bin/python3
"""
Created on Friday July 10 10:19:04 2020
@author: Isaac Stalley

Matriz class, takes 2 parameters for rows and columns and creates a matrix,
contains useful methods for modifying the matrices, like adding and subtracting
them or printing them.
"""


class Matriz():
    # Constructor method, takes in the row and column parameters to create a
    # matrix instance.
    def __init__(self, n, m):
        try:
            self.n = n
            self.m = m
            self.matriz = []
            for i in range(n):
                self.matriz.append([])
                for x in range(m):
                    self.matriz[i].append(0)
        except TypeError:
            print("Parametros deben ser numeros enteros.")

    # Modified __str__ method to return a string for this object type.
    def __str__(self):
        string = ""
        for i in self.matriz:
            for x in i:
                string = string + str(x)
            string = string + "\n"
        return string[:-1]

    # Get method, used to get the coordinate of the matrix instance.
    def get(self, f, c):
        try:
            return self.matriz[f][c]
        except TypeError:
            print("Parametros deben ser numeros enteros.")
        except IndexError:
            print("Coordenada inexistente.")

    # Set method, used to set the value at the coordinate of the matrix
    # instance to some value n.
    def set(self, f, c, n):
        try:
            self.matriz[f][c] = n
        except TypeError:
            print("Parametros deben ser numeros enteros.")
        except IndexError:
            print("Coordenada inexistente.")

    # Modified __add__ method so that this object type can be added.
    def __add__(self, other):
        if (self.n == other.n and self.m == other.m):
            temp = Matriz(self.n, self.m)
            for i in range(len(self.matriz)):
                for x in range(len(self.matriz[i])):
                    temp.matriz[i][x] = self.matriz[i][x] + other.matriz[i][x]
            return temp
        else:
            print("Matrices deben tener las mismas dimensiones.")

    # Modified __sub__ method so that this object type can be subtracted.
    def __sub__(self):
        if (self.n == other.n and self.m == other.m):
            temp = Matriz(self.n, self.m)
            for i in range(len(self.matriz)):
                for x in range(len(self.matriz[i])):
                    temp.matriz[i][x] = self.matriz[i][x] - other.matriz[i][x]
            return temp
        else:
            print("Matrices deben tener las mismas dimensiones.")
