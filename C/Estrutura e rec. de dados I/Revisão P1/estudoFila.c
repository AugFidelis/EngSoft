#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct No{
    int dado;
    struct No *proximo;
};

struct Fila{
    struct No *inicio;
    struct No *fim;
};

void insert(struct Fila *fila, int valor){
    struct No *novo = (struct No*) malloc(sizeof(struct No));

    novo->dado = valor;
    novo->proximo = NULL;

    if(fila->inicio == NULL){
        fila->inicio = novo; 
        //Caso a fila estiver vazia, o marcador de inicio 
        //vai ser o novo (além do fim depois também já que é só um item)
    }
    else{
        fila->fim->proximo = novo; 
        //Caso não estiver vazia, substitui o NULL que é o próximo depois do fim atualmente
    }
    fila->fim = novo; //Independente atualiza o marcador de fim para o fim da fila (o novo nó)

}

int remover(struct Fila *fila){
    if(fila->inicio == NULL){
        printf("Fila vazia!\n");
        return -1;
    }

    struct No *noRemovido = fila->inicio;
    int copiaDados = fila->inicio->dado;

    fila->inicio = fila->inicio->proximo;

    if(fila->inicio == NULL){
        fila->fim = NULL;
    }

    free(noRemovido);

    return copiaDados;

}

void printFila(struct Fila *fila){
    struct No *noAtual = fila->inicio;

    if(noAtual == NULL){
        printf("\nA fila esta vazia.\n");
        return;
    }

    while(noAtual != NULL){
        printf("%d -> ",noAtual->dado);
        noAtual = noAtual->proximo;
    }
    printf("NULL\n");

    return;

}

void liberarFila(struct Fila *fila){
    struct No *noAtual = fila->inicio;

    if(noAtual == NULL){
        printf("\nA fila esta vazia.\n");
        return;
    }

    while(noAtual != NULL){
        struct No *noRemovido = noAtual;

        noAtual = noAtual->proximo;

        free(noRemovido);
    }

    fila->inicio = NULL;
    fila->fim = NULL;
}

int main(){
    struct Fila *fila = (struct Fila*) malloc(sizeof(struct Fila));
    fila->inicio = NULL;
    fila->fim = NULL;
    
    //Inicializa a fila antes de enviá-la para as funções

    // Inserindo elementos na fila
    insert(fila, 10);
    insert(fila, 20);
    insert(fila, 30);

    // Imprimindo a fila
    printFila(fila);

    // Removendo um elemento da fila
    int removido = remover(fila);
    printf("Removido: %d\n", removido);

    // Imprimindo novamente
    printFila(fila);

    // Liberando toda a fila no final
    liberarFila(fila);

    return 0;
}