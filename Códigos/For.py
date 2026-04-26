#"for" é usado para repetir um número específico de vezes.

print('"for in range" repete uma quantidade definida de vezes.\n')

x = int(input("Digite um número para mostrar ele do começo até o final: "))
for i in range(x + 1): #o + 1 adiciona um espaço a mais no final, pois o range começa no 0.
    print(f"Repetição: {i}")
print()
x = int(input("Digite um número para mostrar ele do 1 até o final: "))
for i in range(x): 
    print(f"Repetição: {i + 1}") #o + 1 pula um espaço, fazendo o range que começava no 0, começar no 1.

#############################################################################

print('\n"for" com início, fim e passo.\n')

for i in range(1, 11, 2):
    print(f"Número: {i + 1}")

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

input("\nAperte qualquer coisa para fechar...")