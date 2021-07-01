#include <stdio.h>
#include <stdlib.h>
/*
Created on Sun July 5 10:30:04 2020
@author: Isaac Stalley

GCD program, takes in two int arguments and
calculates the greatest common divisor.
*/
int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        printf("Menos argumentos de la cuenta.\n");
        return 0;
    }
    if (argc > 3)
    {
        printf("Mas argumentos de la cuenta.\n");
        return 0;
    }
    int x = atoi(argv[1]);
    int y = atoi(argv[2]);

    if (x < 0 || y < 0)
    {
        printf("Numeros x o y negativos.\n");
        return 0;
    }
    while (x != y)
    {
        if (x == 0 || y == 0)
        {
            x = 0;
            y = 0;
        }
        if (x > y)
        {
            x -= y;
        }
        else
        {
            y -= x;
        }
    }
    printf("MCD es: %d\n", x);
    return 0;
}
