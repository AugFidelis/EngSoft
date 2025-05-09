#include <stdio.h>

int main(){
    int valor;
    int valor2;

    printf("Digite um numero:\n1- Bom dia\n2- Boa tarde\n3- Boa noite\n");
    scanf("%d",&valor);
    scanf("%d",&valor2);

    if(valor == 1){
        printf("Bom dia");
    }
    else if(valor == 2){
        printf("Boa tarde");
    }
    else{
        printf("Boa noite");
    }

    if(valor > 0 && valor2 == 1){ // || é usado para "ou" e && para "e"
        printf(" e Boas festas");
    }

    return 0;
}