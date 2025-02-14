#include <stdio.h>

int main(){
    int dividendo,divisor,quoc,resto;

    printf("Insira o dividendo:");
    scanf("%d",&dividendo);

    printf("Insira o divisor:");
    scanf("%d",&divisor);

    quoc = dividendo / divisor;
    resto = dividendo % divisor;

    printf("\nDividendo: %d\nDivisor: %d\nQuociente: %d\nResto: %d\n",dividendo, divisor, quoc, resto);

    return 0;
}