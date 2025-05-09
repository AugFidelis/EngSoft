#include <stdio.h>

int main(){
    int valor;

    printf("Digite um numero:\n");
    scanf("%d",&valor);

    if(valor <= 5){
        switch(valor){
            case 0: printf("ZERO");
                break;
            case 1: printf("UM");
                break;
            case 2: printf("DOIS");
                break;
            case 3: printf("TRES");
                break;
            case 4: printf("QUATRO");
                break;
            case 5: printf("CINCO");
                break;
        }

        printf(" ");

        switch(valor){
            case 2: case 4: printf("PAR"); break; 
            //vários casos podem ser colocados juntos para o mesmo resultado
            case 1: case 3: case 5: printf("IMPAR"); break; 
        }

        switch(valor % 2){ //expressões aritméticas podem ser usadas para a expressão do switch
            case 0: printf(" ,RESTO ZERO = PAR"); break;
            case 1: printf(" ,RESTO 1 = IMPAR"); break;
        }
    }
    else{
        printf("Digite um numero menor que 6.");
    }
}