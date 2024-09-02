cidade = "Indaiatuba"
tempo_cidade = 18.415609
trabalho = "Lugar nenhum"
tempo_trabalho = 1

print("Eu moro em {} há {} anos e trabalho em {} há {} anos." .format(cidade, tempo_cidade, trabalho, tempo_trabalho))

print("Eu moro em {2} há {0} anos e trabalho em {3} há {1} anos." .format(cidade, tempo_cidade, trabalho, tempo_trabalho))

print("Eu moro em {} há {:.2f} anos e trabalho em {} há {:03d} anos." .format(cidade, tempo_cidade, trabalho, tempo_trabalho))

print(f"Eu moro em {cidade} há {tempo_cidade} anos e trabalho em {trabalho} há {tempo_trabalho} anos.")