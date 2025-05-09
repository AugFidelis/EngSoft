#include <stdio.h>

void ler_vetor(float v[], int *n);
float calc_media(float v[], int n); //Protótipos, são chamados antes e terminam com ; para declarar as funções

int main(){

    int tamanho;
    float notas[50];

    ler_vetor(notas, &tamanho);

    calc_media(notas, tamanho);

    return 0;
}

void ler_vetor(float v[], int *n){ //Recebe o endereço de 'notas'
    printf("Quantas notas vao ser calculadas?\n");
    scanf("%d", n); 
    //Sem o & no scanf ele se refere ao endereço, no caso é necessário pois n é o endereço de notas

    for(int i = 0; i < *n; i++){ 
        //Se refere ao conteúdo do endereço do n, então tem que ser o *n senão a comparação seria com o número do endereço e não o valor real
        printf("Nota %d: ",i+1);
        scanf("%f",&v[i]);
    }
}

float calc_media(float v[], int n){
    float soma, media;
    for(int i = 0; i < n; i++){
        soma += v[i];
    }
    media = soma / n;
    printf("Media: %.2f", media);
}