#ifndef MAT_LOG_1_KNF_H
#define MAT_LOG_1_KNF_H

const int N=100;

void inputDNF(int arrayOfLiterals[][N], char* literals, int brackets, int numberLiterals);
void outputFormula(int arrayOfLiterals[][N], char* literals, int brackets, int numberLiterals);
void outputTable(int arrayOfLiterals[][N], char *literals, bool *function, int brackets, int numberLiterals);
void outputFalse(char *b, bool* function, int numberLiterals);

#endif //MAT_LOG_1_KNF_H