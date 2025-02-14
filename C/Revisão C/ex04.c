#include <stdio.h>

int main(){

    int num;
    char caractere;

    printf("Insira um numero: ");
    scanf("%d",&num);

    fflush(stdin); //Necessário para scan de caractere depois de scan de número senão ele lê o enter e pula o de caractere

    printf("Insira um caractere: ");
    scanf("%c",&caractere);
    //Também poderia ser usado o getchar() pq já faz a limpeza do stream

}