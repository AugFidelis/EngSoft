#include <stdio.h>

int main(){
    float n1, n2;

    printf("Insira dois numeros: ");
    scanf("%f",&n1);
    scanf("%f",&n2);

    float mult, div, soma, sub;;

    soma = n1 + n2;
    sub = n1 - n2;
    mult = n1 * n2;
    div = n1 / n2;

    printf("Soma: %.2f\nSubtracao: %.2f\nMultiplicacao: %.2f\nDivisao: %.2f", soma, sub, mult, div);
}