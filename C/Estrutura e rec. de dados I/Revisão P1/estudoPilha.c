#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct No{
    int dado;
    struct No *proximo;
};

struct Pilha{
    struct No *topo;
};

void push(struct Pilha *pilha, int valor){
    struct No *novoNo = (struct No*) malloc(sizeof(struct No));

    novoNo->dado = valor;
    novoNo->proximo = pilha->topo;

    pilha->topo = novoNo;

}

int pop(struct Pilha *pilha){
    if(pilha->topo == NULL){
        printf("Pilha vazia!\n");
        return -1;
    }
    
    int info = pilha->topo->dado;

    struct No *noRemovido = pilha->topo;
    pilha->topo = pilha->topo->proximo;

    free(noRemovido);

    return info;
}

int main(){
    struct Pilha *pilha = malloc(sizeof(struct Pilha));
    pilha->topo = NULL;

    // Usa push(pilha, valor) e pop(pilha)
    push(pilha, 10);
    push(pilha, 20);
    int valorRemovido = pop(pilha);
    printf("Valor removido: %d\n", valorRemovido);

    free(pilha); // libera a memória da pilha se usou malloc

    return 0;
}