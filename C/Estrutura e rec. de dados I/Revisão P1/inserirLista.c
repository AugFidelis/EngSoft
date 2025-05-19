#include <stdio.h>

struct No{
    int dado;
    struct No *proximo;
};

void inserirInicio(struct No **cabeca, int info){ 
    // **cabeca é por que ele ta apontando pro ponteiro, como se fosse um *(*cabeca) do *cabeca original no int main()
    
    struct No *novoNo = malloc(sizeof(struct No)); 
    // *novoNo é um ponteiro porque o malloc() devolve o endereço da onde ele alocou o espaço

    novoNo->dado = info;
    novoNo->proximo = *cabeca; //*cabeca vai apontar para o início anterior da lista (novoNo --> cabeca --> NULL)

    *cabeca = novoNo; 
    //novoNo não tem o ponteiro aqui pra receber o endereço guardado como conteúdo dele, 
    //não para receber o que ele está apontando
}



int main(){
    struct No *cabeca = NULL; //Passo 1: A lista começa apontando para nada, nada foi adicionado ainda

    inserirInicio(&cabeca, 10); 
    //O & é necessário aqui para que o ponteiro da função possa apontar para o *cabeca para conseguir modificá-lo,
    //senão ele não mudaria a cabeça e nada mudaria na lista 
}