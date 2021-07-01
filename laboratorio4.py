#!/usr/bin/python3
"""
Created on Mon June 16 4:19:04 2020
@author: Isaac Stalley

Fibonacci program, takes a user input and recursively calculates
and returns it's fibonacci counterpart.
"""
import argparse
import time
start_time = time.time()


# Fibonacci function, takes in a parameter n and returns the
# fibonacci of n.
def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Defines parser arguments, one position argument for the fibonacci
# number and two optional arguments for time and whether or not to
# return the complete list of fibonacci numbers.
parser = argparse.ArgumentParser()
parser.add_argument("posicion",
                    help="posicion is the desired fibonacci number")
parser.add_argument("-t", "--tiempo",
                    help="prints the total run time of the instance",
                    action="store_true")
parser.add_argument("-c", "--completa",
                    help="prints the complete fibonacci list up to the"
                         " specified number",
                    action="store_true")
args = parser.parse_args()

# Checks and prints if user wants the full list of fibonacci numbers.
if args.completa:
    for i in range(int(args.posicion) + 1):
        print("Fibonacci[" + str(i) + "] = " + str(fibonacci(int(i))))
else:
    print("Fibonacci[" + args.posicion + "] = "
          + str(fibonacci(int(args.posicion))))

# Checks and calculates if the user wants the total run time of the program.
if args.tiempo:
    print("Total execution time: %s seconds" % (time.time() - start_time))
