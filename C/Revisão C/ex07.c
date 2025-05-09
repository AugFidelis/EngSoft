#include <stdio.h>

int main(){
    int n, k;
    
    printf("Ate onde vai?");
    scanf("%d",&n);

    while(k <= n){
        printf("%d ",k);
        k++;
    }

    printf("\n");

    for(int i = 0;i <= n;i++){
        printf("%d ",i);
    }

    return 0;
}