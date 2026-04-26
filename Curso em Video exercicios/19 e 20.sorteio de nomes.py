import random

print("Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.\n")

print("Nomeie quatro alunos.")
nomes = []
for i in range(4):
    nome = input(f"Digite o nome do {i + 1} aluno: ").strip()
    while not nome.replace(" ", "").isalpha():
        print("Nomes possuem somente letras.")
        nome = input("Digite um nome: ").strip()
    nomes.append(nome)
       
print(f"o aluno escolhido aleatoriamente foi: {random.choice(nomes)}\n")

print("agora com os alunos sorteados, o professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.\n")

random.shuffle(nomes)
print(f"A ordem da apresentação será: {nomes}")

input("\nAperte qualquer coisa para fechar...")