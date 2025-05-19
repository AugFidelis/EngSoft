#include <stdio.h>

struct Aluno{
    char nome[50];
    int idade;
    float notaFinal;
};

void imprimeAluno(struct Aluno *p_aluno){
    printf("Nome do aluno: %s\n", p_aluno->nome);
    printf("Idade do aluno: %d\n", p_aluno->idade);
    printf("Nota final do aluno: %.1f\n", p_aluno->notaFinal);
}

void atualizaNota(struct Aluno *p_aluno){
    float nova_nota;
    printf("Insira a nova nota do aluno: ");
    scanf("%f",&nova_nota);
    p_aluno->notaFinal = nova_nota;
}

int main(){
    struct Aluno aluno;

    printf("Insira os dados do aluno:\nNome: ");
    gets(aluno.nome);
    
    printf("Idade: ");
    scanf("%d",&aluno.idade);

    printf("Nota final: ");
    scanf("%f",&aluno.notaFinal);

    imprimeAluno(&aluno);

    int opc;
    printf("Deseja alterar a nota do aluno? Digite 1 para sim: ");
    scanf("%d",&opc);

    if(opc == 1){
        atualizaNota(&aluno);
        imprimeAluno(&aluno);
    }
}