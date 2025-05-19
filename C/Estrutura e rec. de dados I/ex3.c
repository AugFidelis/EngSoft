#include <stdio.h>

int main() {
    int numero, i, ehPrimo = 1; // ehPrimo = 1 significa que o número é primo inicialmente

    // Entrada do número
    printf("Digite um numero inteiro: ");
    scanf("%d", &numero);

    // Números menores que 2 não são primos
    if (numero < 2) {
        ehPrimo = 0;
    } else {
        // Verifica divisores de 2 até a raiz quadrada de "numero"
        for (i = 2; i * i <= numero; i++) {
            if (numero % i == 0) {
                ehPrimo = 0; // Encontrou um divisor, não é primo
                break;
            }
        }
    }

    // Imprime o resultado
    if (ehPrimo) {
        printf("O numero %d eh primo.\n", numero);
    } else {
        printf("O numero %d nao eh primo.\n", numero);
    }

    return 0;
}