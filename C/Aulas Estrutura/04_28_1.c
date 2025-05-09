#include <stdio.h>

//Listas encadeadas

struct No{
    int dado;
    struct No *proximo;
};

struct No* inserirFront(struct No *lista, int valor){
    struct No *novo = (struct No*) malloc(sizeof(struct No));
    novo->dado = valor;
    novo->proximo = lista;
    return novo;
}

int main(){
    //struct No *lista = NULL;

    //malloc()

    //lista = inserirFront(lista, 1);
    //lista = inserirEnd(lista, 6);

}