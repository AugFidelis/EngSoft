# Você foi contratado por uma escola para fazer o seguinte script em Python:
# Primeiro, pergunta a quem vai usar o script quantos alunos tem na sala.
# Depois, quantas matérias cada aluno estuda. Em seguida o usuário vai
# preenchendo a nota de cada matéria, de cada aluno. Seu programa deve fornecer
# a média de cada aluno e a média geral da turma.

num_alunos = int(input("Quantos alunos há na sala? "))
num_mat = int(input("Quantas matérias cada aluno estuda? "))

for i in range(1,num_alunos+1):
    print(f"Aluno {i}:")

    for j in range(1,num_mat+1):
        print(f"Nota")
