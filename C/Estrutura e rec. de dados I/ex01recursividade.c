#include <stdio.h>
#include <stdbool.h>

void vetorcresc(int n, int vetor[]) {
    bool swap = false;

    for (int i = 1; i < n; i++) {
        if (vetor[i] < vetor[i - 1]) {
            int temp = vetor[i - 1];
            vetor[i - 1] = vetor[i];
            vetor[i] = temp;

            swap = true;
        }
    }

    if (swap == true) {
        vetorcresc(n, vetor);
    }
}

int main() {
    int vetorteste[6] = {4, 6, 2, 1, 7, 3};

    vetorcresc(6, vetorteste);

    for (int i = 0; i < 6; i++) {
        printf("%d ", vetorteste[i]);
    }

    return 0;
}