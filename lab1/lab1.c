#include <stdbool.h>
#include "lab1.h"

void inputDNF(int arrayOfLiterals[][N], char *literals, int brackets, int numberLiterals) {
    int i = 0, j = 0;
    printf("Введите литералы: ");
    for (i = 0; i < numberLiterals; i++)
        scanf("%s", &literals[i]);
    printf("Литерал есть: 1");
    printf("\nЛитерал c отрицанием: -1");
    printf("\nОтсутствие литерала: 0\n");
    for (i = 0; i < brackets; i++)
        for (j = 0; j < numberLiterals; j++)
            scanf("%d", &arrayOfLiterals[i][j]);
}

void outputFormula(int arrayOfLiterals[][N], char *literals, int brackets, int numberLiterals) {
    int i = 0, j = 0;
    for (i = 0; i < brackets; i++) {
        printf("(");
        j = 0;
        while ((arrayOfLiterals[i][j] == 0) && (j < numberLiterals))
            j++;
        if (j < numberLiterals) {
            if (arrayOfLiterals[i][j] == -1)
                printf("!%c", literals[j]);
            else
                printf("%c", literals[j]);
        }
        j++;
        for (j; j < numberLiterals; j++) {
            if (arrayOfLiterals[i][j] == -1)
                printf(" & !%c", literals[j]);
            if (arrayOfLiterals[i][j] == 1)
                printf(" & %c", literals[j]);
        }
        printf(")");
        if (i < brackets - 1) {
            printf(" V ");
        }
    }
    printf("\n");
}

void outputTable(int arrayOfLiterals[][N], char *literals, bool *function, int brackets, int numberLiterals) {
    for (int i = 0; i < numberLiterals; i++)
        printf("%c\t", literals[i]);
    printf("f\t\n");
    int rows = pow(2, numberLiterals);
    bool table[N];
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < numberLiterals; j++) {
            table[j] = (i >> (numberLiterals - 1 - j)) & 1;
            printf("%d\t", table[j]);
        }
        bool f = 0, x;
        int j = 0, k;
        while (!f && (j < brackets)) {
            x = 1;
            k = 0;
            while (x && (k < numberLiterals)) {
                if (arrayOfLiterals[j][k] == 1)
                    x &= table[k];
                if (arrayOfLiterals[j][k] == -1)
                    x &= !table[k];
                k++;
            }
            f |= x;
            j++;
        }
        function[i] = f;
        printf("%d\t\n", f);
    }
}

void outputFalse(char *literals, bool *function, int numberLiterals) {
    for (int i = 0; i < numberLiterals; i++)
        printf("%c\t", literals[i]);

    printf("f\t\n");
    int all = pow(2, numberLiterals);
    bool table[N];
    for (int i = 0; i < all; i++) {
        if (!function[i]) {
            for (int j = 0; j < numberLiterals; j++) {
                table[j] = (i >> (numberLiterals - 1 - j)) & 1;
                printf("%i\t", table[j]);
            }
            printf("%i\t\n", function[i]);
        }
    }
}