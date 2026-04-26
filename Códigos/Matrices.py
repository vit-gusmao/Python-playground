# Matrizes (listas 2D) armazenam valores em linhas e colunas.

print('"Matrizes (listas 2D)" armazenam valores em linhas e colunas.\n')

matriz = []

while True:
    try:
        linhas = int(input("Digite quantas linhas a matriz terá: "))
        if linhas <= 0:
            print(f"{linhas} é inválido. Digite um número maior que 0.")
            continue
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")

while True:
    try:
        colunas = int(input("Digite quantas colunas a matriz terá: "))
        if colunas <= 0:
            print(f"{colunas} é inválido. Digite um número maior que 0.")
            continue
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")

for i in range(linhas):
    linha = []
    for j in range(colunas):
        while True:
            try:
                valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro válido.")
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz completa:")
for linha in matriz:
    print(linha)
print()

#############################################################################

print("Acessando elementos da matriz.\n")

print(f"Primeiro elemento [0][0]: {matriz[0][0]}")
print(f"Último elemento [-1][-1]: {matriz[-1][-1]}\n")

#############################################################################

print("Percorrendo matriz com for.\n")

for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        print(f"Posição [{i}][{j}] = {valor}")

print("Fim da matriz.\n")

#############################################################################

print("Verificando se valor está na matriz.\n")

while True:
    try:
        buscar = int(input("Digite um valor para buscar: "))
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")

posicoes = []
for i, linha in enumerate(matriz):
    for j, valor in enumerate(linha):
        if valor == buscar:
            posicoes.append((i, j))

if posicoes:
    print(f"{buscar} está na matriz nas posições: {posicoes}\n")
else:
    print(f"{buscar} NÃO está na matriz.\n")

#############################################################################

print("Verificando o maior e menor valor da matriz usando max() e min().\n")

todos_os_valores = [valor for linha in matriz for valor in linha]
maior = max(todos_os_valores)
menor = min(todos_os_valores)

print(f"O maior valor da matriz é {maior}.")
print(f"O menor valor da matriz é {menor}.\n")

input("Aperte qualquer coisa para fechar...")

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