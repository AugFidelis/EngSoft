#include <stdio.h>
#include <math.h>

int main(){
    /* Comentário */
    printf("Hello World\n");

    int var1;
    float varquad;

    //char umcaractere; /*char só recebe um caractere*/

    scanf("%d",&var1);

    varquad = sqrt(var1);

    printf("%.2f",varquad);

    return 0;
}   