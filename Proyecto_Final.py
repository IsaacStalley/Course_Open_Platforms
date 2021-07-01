#!/usr/bin/python3
"""
Created on Mon June 16 4:19:04 2020
@author: Isaac Stalley

Graphing program, graphs a function and optionally it's first and second
derivative. Accepts parameters through the terminal using argparse or
optionally through an interactive terminal.
"""
import argparse
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
x = symbols('x')


# Argparse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--guardar",
                    help="Guardar gráfica en un archivo dado por este"
                         " parámetro.")
parser.add_argument("-i", "--limite_inferior",
                    type=float,
                    help="Límite inferior del dominio.")
parser.add_argument("-s", "--limite_superior",
                    type=float,
                    help="Límite superior del dominio.")
parser.add_argument("-p", "--paso",
                    type=float,
                    help="La diferencia entre cada valor de x.")
parser.add_argument("-c", "--cifras_significativas",
                    type=int,
                    help="La cantidad de cifras significativas de los"
                         " resultados.")
parser.add_argument("-d", "--derivadas",
                    type=int,
                    help="Proporcionado si se desea graficar la primera"
                         " o segunda derivada de 'y'.",
                    choices=[0, 1, 2],)
parser.add_argument("-e", "--archivo_entrada",
                    help="Archivo de entrada, en la primera linea debe estar"
                         " escrita la expresion matematica por graficar.")
parser.add_argument("-t", "--terminal_interactiva",
                    help="Activa la terminal interactiva donde proporcionara"
                         " al usuario los parametros anteriores.",
                    action="store_true")
args = parser.parse_args()


# Calculates y values of an array of x values and stores them in a list,
# also checks for points that aren't real.
def ycalc(f, x_range, c):
    y = []
    for i in x_range:
        t = f.subs(x, i).evalf(c)
        if t.is_real:
            y.append(t)
        else:
            print("Punto invalido en x = " + str(i) + " para: " + str(f))
            y.append(None)
    return y


# Graphing function, takes in the user parameters and graphs the functions
# using matplotlib.
def graphingFunction(f, d, lf, ls, p, c, g):
    x_range = np.arange(lf, ls + p, p)
    dy = diff(f, x)
    dy_dy = diff(f, x, 2)
    y = ycalc(f, x_range, c)
    dy_list = ycalc(dy, x_range, c)
    dy_dy_list = ycalc(dy_dy, x_range, c)
    if d == 0:
        plt.plot(x_range, y)
        plt.grid()
        plt.ylim([lf/2, ls/2])
    if d >= 1:
        fig, axs = plt.subplots(d + 1)
        axs[0].plot(x_range, y)
        axs[1].plot(x_range, dy_list, 'tab:red')
        axs[0].grid()
        axs[1].grid()
        axs[0].set_ylim([lf/2, ls/2])
        axs[1].set_ylim([lf/2, ls/2])
    if d == 2:
        axs[2].plot(x_range, dy_dy_list, 'tab:green')
        axs[2].grid()
        axs[2].set_ylim([lf/2, ls/2])
    plt.show()
    if g is not None:
        try:
            fig.savefig(g)
        except Exception:
            print("Direccion o nombre invalido para guardar")


# dataCheck function, checks that the user's inputs meets all the
# requirements before calling the graphing function.
def dataCheck(f, d, lf, ls, p, c, g):
    required = ["Funcion", "Cifras Significativas", "Limite Inferior",
                "Limite Superior", "Pasos"]
    counter = 0
    for i in (f, c, lf, ls, p):
        if i is None:
            print("Parametro requerido: " + required[counter])
            exit()
        counter += 1
    if args.terminal_interactiva is False:
        try:
            entry = open(f, "r")
        except Exception:
            print("El archivo de entrada es inexistente, o no tiene permisos"
                  " de lectura.")
            exit()
        f = entry.readline().strip()
        entry.close()
    try:
        function = parse_expr(f)
    except Exception:
        print("La expresión matemática es inválida")
        exit()
    if d is None:
        d = 0
    if d > 2:
        print("Solo se graficará hasta la segunda derivada.")
        d = 2
    if ls <= lf:
        print("El limite superior debe ser mayor al limite inferior")
        exit()
    if c <= 0:
        print("Cifras significativas deben ser mayor a 0")
        exit()
    if p <= 0:
        print("Paso debe ser mayor a 0")
        exit()
    if p > ls - lf:
        print("Paso debe ser menor al rango de x")
        exit()
    graphingFunction(function, d, lf, ls, p, c, g)


# Interactive terminal, asks the user for required and optional inputs.
if args.terminal_interactiva:
    try:
        f = input("Ingrese la expresion matematica de 'y' para graficar:")
        g = input("Ingrese el archivo donde quiere guardar la grafica"
                  " [puede dejarlo vacio]:")
        lf = float(input("Ingrese el limite inferior de 'x':"))
        ls = float(input("Ingrese el limite superior de 'x':"))
        p = float(input("Ingrese el paso (diferencia entre cada 'x'):"))
    except ValueError:
        print("Input invalido, deber ser tipo: Float")
        exit()
    try:
        c = int(input("Ingrese la cantidad de cifras significativas:"))
        d = int(input("Derivadas por graficar [0, 1, 2]\n(0 = ninguna, 1 = "
                      "primer derivada, o 2 = segunda derivada)[puede dejarlo"
                      " vacio]:"))
    except ValueError:
        print("Input invalido, deber ser tipo: Int")
        exit()
    dataCheck(f, d, lf, ls, p, c, g)
else:
    dataCheck(args.archivo_entrada, args.derivadas, args.limite_inferior,
              args.limite_superior, args.paso, args.cifras_significativas,
              args.guardar)
