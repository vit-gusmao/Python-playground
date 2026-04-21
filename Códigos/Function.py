# Funções servem para reutilizar código e organizar melhor o programa.

print('"def" cria uma função que pode ser usada várias vezes.\n')

def saudacao():
    print("Olá! Essa é uma função simples.\n")

# chamando a função
saudacao()

#############################################################################

print('Função com parâmetros (entrada de dados).\n')

def mostrar_nome(nome):
    print(f"Seu nome é: {nome}\n")

nome_usuario = input("Digite seu nome: ")
mostrar_nome(nome_usuario)

#############################################################################

print('Função com retorno (return).\n')

def somar(a, b):
    resultado = a + b
    return resultado  # retorna o valor para fora da função

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = somar(n1, n2)
print(f"A soma é: {soma}\n")

#############################################################################

print('Função com validação usando try/except.\n')

def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero  # retorna quando for válido
        except ValueError:
            print("Valor inválido! Digite um número válido.\n")

# usando a função
n1 = ler_numero("Digite um número: ")
n2 = ler_numero("Digite outro número: ")

print(f"A soma entre {n1} e {n2} é: {n1 + n2}\n")

#############################################################################

print('Função pode ser chamada várias vezes.\n')

for i in range(3):
    num = ler_numero(f"Digite o {i+1}º número: ")
    print(f"Você digitou: {num}\n")

#############################################################################

input("Aperte qualquer coisa para fechar...")