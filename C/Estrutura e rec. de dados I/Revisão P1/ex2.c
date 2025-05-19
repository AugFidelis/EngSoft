#include <stdio.h>

int main(){
    char caractere;

    printf("Insira um caractere:");
    scanf("%c", &caractere);

    if(caractere == 'a' || caractere == 'e' || caractere == 'i' || caractere == 'o' || caractere == 'u'){
        printf("Vogal");
    }
    else{
        printf("Consoante");
    }
}