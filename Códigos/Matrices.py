# Matrizes são listas dentro de listas.

print('"Matrizes" são listas dentro de listas.\n')

linhas = 3
colunas = 3

matriz = []

#############################################################################

print('Criando matriz com valores do usuário.\n')

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print(f"\nMatriz completa: {matriz}\n")

#############################################################################

print('Acessando elemento da matriz.\n')

print(f"Elemento [0][0]: {matriz[0][0]}\n")

#############################################################################

print('Percorrendo matriz.\n')

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

print("\nFim da matriz.\n")

#############################################################################

print('Somando todos os valores da matriz.\n')

soma = 0

for linha in matriz:
    for elemento in linha:
        soma += elemento

print(f"Soma total: {soma}\n")

#############################################################################

input("Aperte qualquer coisa para fechar...")