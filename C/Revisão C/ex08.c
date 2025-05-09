#include <stdio.h>

int main(){
    int matriz[2][3];

    for(int i = 0;i<2;i++){
        for(int j = 0;j<3;j++){
            printf("Matriz[%d][%d]: ",i,j);
            scanf("%d",&matriz[i][j]);
            printf("\n");
        }
    }

    for(int i = 0;i<2;i++){
        for(int j = 0;j<3;j++){
            printf("[%d][%d]: %d ",i,j,matriz[i][j]);
        }
        printf("\n");
    }

    return 0;
}