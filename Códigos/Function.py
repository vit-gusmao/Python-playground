# Funções servem para reutilizar código e organizar melhor o programa.

print('"def" cria uma função que pode ser usada várias vezes.\n')

def saudacao():
    print("Saudações.\n")

# chamando a função
saudacao()

#############################################################################

print('Função com variáveis.\n')

def mostrar_nome(nome):
    print(f"Seu nome é: {nome}\n")

nome_usuario = input("Digite seu nome: ")
mostrar_nome(nome_usuario)

#############################################################################

print('Função com listas, while, try/except e validação de número inválido.\n')

num = []

while True:
    try:
        num = []
        for i in range(2):
            n = float(input(f"Digite o {i+1}º número: "))
            num.append(n)
        break  # saiu do loop se conseguiu ler corretamente os dois números
    except ValueError:
        print("Valor inválido! Digite números válidos.\n")

numf = [int(n) if n.is_integer() else n for n in num]
print(f"Lista dos números digitados (formatados): {numf}")
print(f"A soma entre {numf[0]} e {numf[1]} é: {numf[0] + numf[1]}\n")

#############################################################################

print('Função pode ser usada para múltiplos números também.\n')

num = []
while True:
    try:
        num = []
        for i in range(3):
            n = float(input(f"Digite o {i+1}º número: "))
            num.append(n)
        break
    except ValueError:
        print("Valor inválido! Digite números válidos.\n")

numf = [int(n) if n.is_integer() else n for n in num]
print(f"Lista dos números digitados (formatados): {numf}")

for i, n in enumerate(numf):
    print(f"Você digitou [{i+1}]: {n}")

#############################################################################

input("Aperte qualquer coisa para fechar...")