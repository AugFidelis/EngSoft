#include <stdio.h>
#include <stdlib.h>

struct No{
    int dado;
    struct No *proximo;
};

//------------------------------------------------------------------------------------------------------------------

struct No* inserirFront(int info, struct No *cabeca){

    struct No *novoNo = (struct No*) malloc(sizeof(struct No)); 
    //(struct No*) é um cast para o malloc, obrigatório em C++

    novoNo->dado = info;
    novoNo->proximo = cabeca;

    return novoNo;

}

//------------------------------------------------------------------------------------------------------------------

struct No* inserirEnd(int info, struct No *cabeca){
    
    struct No *novoNo = (struct No*) malloc(sizeof(struct No));

    novoNo->dado = info;
    novoNo->proximo = NULL;

    // Quando o ponteiro cabeca é NULL, isso significa que ele não está apontando para lugar nenhum.
    // Em outras palavras, o próprio valor armazenado em cabeca (que representa o endereço) é NULL.
    
    if(cabeca == NULL){ //Caso o cabeca apontar pra NULL
        return novoNo; //Já retorna o novoNo pois ele já está no final e vai virar a cabeca
    }
    else{
        struct No *noAtual = cabeca;

        //Enquanto o nó atual (começa na cabeça) não for nulo (está no fim), 
        //ele vira o próximo para andar para frente na lista
        while(noAtual->proximo != NULL){ 
            noAtual = noAtual->proximo;
        }

        //Ao chegar no fim, ele muda o proximo de null (fim atual) para 
        //o novo nó, que será o novo a apontar pra NULL
        noAtual->proximo = novoNo;
        return cabeca;
    }
}

//------------------------------------------------------------------------------------------------------------------

struct No* inserirIntermed(int info, struct No *cabeca, int posicao){
    struct No *novoNo = (struct No*) malloc(sizeof(struct No));

    novoNo->dado = info;

    if(posicao == 0){ //Caso for colocar no começo faz q nem o inserirFront
        novoNo->proximo = cabeca;
        return novoNo;
    }

    struct No *noAtual = cabeca;

    int contador = 0;
    while(contador < posicao-1 && noAtual->proximo != NULL){
        noAtual = noAtual->proximo;
        contador++;
    }

    if (noAtual == NULL) {
        printf("Posição inválida!\n");
        free(novoNo);
        return cabeca;
    }

    novoNo->proximo = noAtual->proximo; 
    //Faz o novo nó TAMBÉM apontar pro que tá na frente dele sem alterar a lista original
    
    noAtual->proximo = novoNo;
    //Muda o próximo do nó antes do Novo nó para conectar o Novo nó na lista

}

//------------------------------------------------------------------------------------------------------------------

struct No* removerFront(struct No *cabeca){
    if(cabeca == NULL){
        printf("A lista já está vazia!");
        return cabeca;
    }

    struct No *noRemovido = cabeca;

    cabeca = cabeca->proximo; //A nova cabeça agora é o segundo (próximo) da lista

    free(noRemovido); //Libera o espaço da memória sendo consumido pelo nó que foi removido

    return cabeca;
}

//------------------------------------------------------------------------------------------------------------------

struct No* removerEnd(struct No *cabeca){
    if(cabeca == NULL){
        printf("A lista já está vazia!");
        return cabeca;
    }

    if(cabeca->proximo == NULL){
        free(cabeca);
        return NULL;
    }

    struct No *noAtual = cabeca;
    struct No *proximoNo = noAtual->proximo;

    while(proximoNo->proximo != NULL){
        noAtual = noAtual->proximo;
        proximoNo = proximoNo->proximo;
    }

    noAtual->proximo = NULL;
    free(proximoNo);

    return(cabeca);
}

//------------------------------------------------------------------------------------------------------------------

struct No* removerIntermed(struct No *cabeca, int posicao){
    if(cabeca == NULL){
        printf("Lista vazia!");
        return NULL;
    }

    if(posicao == 0){ //Caso for 0 (o primeiro item da lista)
        struct No *noRemovido = cabeca;
        cabeca = cabeca->proximo;
        free(noRemovido);
        return cabeca;
    }
    
    struct No *noAnterior = cabeca;
    
    int contador = 0;

    while(contador < posicao-1 && noAnterior != NULL){
        noAnterior = noAnterior->proximo;
        contador++;
    }

    if(noAnterior == NULL || noAnterior->proximo == NULL){ //Caso o nó não conseguir chegar na posição e atingir um null
        printf("Posicao invalida!");
        return cabeca;
    }

    struct No *noRemovido = noAnterior->proximo;

    noAnterior->proximo = noRemovido->proximo;

    free(noRemovido);

    return cabeca;
}

//------------------------------------------------------------------------------------------------------------------

void imprimirLista(struct No *cabeca){
    if(cabeca == NULL){
        printf("A lista está vazia");
        return;
    }
    
    struct No *noAtual = cabeca;
    
    printf("%d",noAtual->dado);
    
    while(noAtual->proximo != NULL){
        noAtual = noAtual->proximo;
        
        printf("-> %d ",noAtual->dado);
    }
}

//------------------------------------------------------------------------------------------------------------------

int main(){
    struct No *cabeca = NULL;

    cabeca = inserirFront(1, cabeca);
    cabeca = inserirFront(2, cabeca);
    cabeca = inserirFront(2, cabeca);
    cabeca = inserirFront(3, cabeca);
    cabeca = inserirFront(4, cabeca);
    cabeca = inserirEnd(20, cabeca); //4 - 3 - 2 - 2 - 1 - 20
    cabeca = inserirIntermed(99, cabeca, 3); 
    imprimirLista(cabeca);

}