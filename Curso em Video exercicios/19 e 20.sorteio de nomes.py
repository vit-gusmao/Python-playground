import random

print("Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.\n")

aluno1 = input("Digite o nome de um aluno: ")
aluno2 = input("Digite o nome de outro aluno: ")
aluno3 = input("Digite o nome de outro aluno: ")
aluno4 = input("Digite o nome de outro aluno: ")
nomes = [aluno1, aluno2, aluno3, aluno4]
print(f"o aluno scolhido aleatoriamente foi: {random.choice(nomes)}\n")

print("agora com os alunos sorteados, o professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.\n")

random.shuffle(nomes)
print(f"A ordem da apresentação será: {nomes}")

input("\nAperte qualquer coisa para fechar...")