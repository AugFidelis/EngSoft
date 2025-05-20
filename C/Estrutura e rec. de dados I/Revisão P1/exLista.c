#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Cliente{
    char nome[50];
    char cpf[15];
    char celular[16];
    struct Cliente *proximo;
};

struct Cliente* cadastrarCliente(struct Cliente *cabeca, char nome[50], char cpf[15], char celular[16]){
    struct Cliente *novoCliente = (struct Cliente*) malloc(sizeof(struct Cliente));

    strcpy(novoCliente->nome, nome);
    strcpy(novoCliente->cpf, cpf);
    strcpy(novoCliente->celular, celular);

    novoCliente->proximo = cabeca;

    printf("\nCliente cadastrado com sucesso!\n");

    return novoCliente;

}

struct Cliente* removerCliente(struct Cliente *cabeca, char cpf[15]){
    if(cabeca == NULL){ //Caso a lista estiver vazia
        printf("Nao ha clientes para remover!");
        return NULL;
    }

    if(strcmp(cabeca->cpf, cpf) == 0){ //Caso o cpf da próprica cabeca (o primeiro) for o que tem q ser excluido
        struct Cliente *clienteRemovido = cabeca;
        cabeca = cabeca->proximo;

        free(clienteRemovido);
        return cabeca;
    }
    
    struct Cliente *clienteAnterior = cabeca;
    struct Cliente *clienteRemovido = clienteAnterior->proximo;

    while(clienteRemovido != NULL && strcmp(clienteRemovido->cpf, cpf) != 0){
        clienteAnterior = clienteRemovido;
        clienteRemovido = clienteRemovido->proximo;
    }

    if(clienteRemovido == NULL){
        printf("\nCliente nao encontrado!\n");
        return cabeca;
    }

    clienteAnterior->proximo = clienteRemovido->proximo;
    free(clienteRemovido);

    printf("\nCliente removido com sucesso!\n");

    return cabeca;
}

struct Cliente* exibirClientes(struct Cliente *cabeca){
    if(cabeca == NULL){
        printf("Lista vazia!");
        return NULL;
    }
    
    struct Cliente *clienteAtual = cabeca;

    printf("Lista de clientes:\n\n");
    while(clienteAtual != NULL){
        printf("Nome: %s | CPF: %s | Celular: %s\n",clienteAtual->nome, clienteAtual->cpf, clienteAtual->celular);

        clienteAtual = clienteAtual->proximo;
    }

    return cabeca;
}

struct Cliente* pesquisarCliente(struct Cliente *cabeca, char cpf[15]){
    if(cabeca == NULL){
        printf("Lista vazia!");
        return NULL;
    }

    struct Cliente *clienteAtual = cabeca;

    while(clienteAtual != NULL && strcmp(clienteAtual->cpf, cpf) != 0){
        clienteAtual = clienteAtual->proximo;
    }

    if(clienteAtual == NULL){
        printf("\nCliente nao encontrado!\n");
        return cabeca;
    }

    printf("\nCliente encontrado!\n");
    printf("Nome: %s | CPF: %s | Celular: %s\n",clienteAtual->nome, clienteAtual->cpf, clienteAtual->celular);

    return cabeca;

}

int main(){
    struct Cliente *cabeca = NULL;

    char nome[50], cpf[15], celular[16];
    int opc;
    while(opc != 5){
        printf("-- Menu de gerenciamento de clientes --\n");
        printf("1) Cadastrar cliente\n2) Excluir cliente\n3) Exibir clientes\n4) Consultar clientes por CPF\n5) Sair do programa\n");
        
        scanf("%d",&opc);

        printf("\n");

        if(opc == 1){
            fflush(stdin);
            
            printf("Nome do cliente: ");
            gets(nome);

            printf("CPF do cliente: ");
            gets(cpf);
            
            printf("Celular do cliente: ");
            gets(celular);
            
            cabeca = cadastrarCliente(cabeca, nome, cpf, celular);
        }
        if(opc == 2){
            fflush(stdin);
            
            printf("CPF do cliente a excluir: ");
            gets(cpf);

            cabeca = removerCliente(cabeca, cpf);
        }
        if(opc == 3){
            cabeca = exibirClientes(cabeca);
        }
        if(opc == 4){
            fflush(stdin);
            
            printf("CPF do cliente a pesquisar: ");
            gets(cpf);

            cabeca = pesquisarCliente(cabeca, cpf);
        }

        printf("\n");
    }
}