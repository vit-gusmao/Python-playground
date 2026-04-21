# "for" é usado para repetir um número específico de vezes.

print('"for in range" repete uma quantidade definida de vezes.\n')

for i in range(5):
    print(f"Repetição: {i}")

print("Fim do loop for.\n")

#############################################################################

print('"for" com início, fim e passo.\n')

for i in range(1, 11, 2):
    print(f"Número: {i}")

print("Fim do loop com passo.\n")

#############################################################################

print('"foreach" (for em listas) percorre elementos diretamente.\n')

nomes = ["Ana", "Carlos", "João"]

for nome in nomes:
    print(f"Nome: {nome}")

print("Fim do foreach.\n")

#############################################################################

print('"for" com índice usando enumerate.\n')

frutas = ["Maçã", "Banana", "Uva"]

for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice} - Fruta: {fruta}")

print("Fim do for com índice.\n")

#############################################################################

input("Aperte qualquer coisa para fechar...")