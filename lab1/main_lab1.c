#include <stdio.h>
#include <windows.h>
#include <stdbool.h>
#include <math.h>
#include "lab1.c"

int main() {
    SetConsoleOutputCP(CP_UTF8);

    printf( "Введите количество скобок: ");
    int brackets;
    scanf("%i", &brackets);

    printf( "Введите количество литералов: ");
    int numberLiterals;
    scanf("%i", &numberLiterals);

    int arrayOfLiterals[N][N];
    char literals[N];
    bool function[N];

    inputDNF(arrayOfLiterals, literals, brackets, numberLiterals);
    outputFormula(arrayOfLiterals, literals, brackets, numberLiterals);
    outputTable(arrayOfLiterals, literals, function, brackets, numberLiterals);
    printf("\n");
    outputFalse(literals, function, numberLiterals);

    return 0;
}