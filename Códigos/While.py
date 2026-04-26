# While repete enquanto a condição for verdadeira.

print('"while" executa enquanto for True.')

num = 0
while True:
    try:
        contador = int(input("Digite um número inteiro para mostrar ele do começo até o final: "))
        break
    except ValueError:
        print("Digite um número inteiro válido.")

while num < contador:
    num += 1
    print(f"Contador: {num}")

print("Fim do loop.\n")

#############################################################################

print('"while True" cria um loop infinito até usar break.')

while True:
    numero = input("Digite '0' para sair: ")

    if numero == "0":
        print("Saindo...\n")
        break
    else:
        print("Você não digitou 0.\n")

#############################################################################

print('"or" Apenas uma condição precisa ser verdadeira.')

while True:
    try:
        n = int(input("Digite um número entre 1 a 10: "))
        while n > 10 or n < 0:
            print(f'O número {n} não está entre 1 a 10.')
            n = int(input("Digite um número entre 1 a 10: "))
        break
    except ValueError:
        print("Digite um número inteiro válido.")

print("Você digitou um número entre 1 a 10.\n")

########################################################################

print('"and" Duas condições precisam ser verdadeiras.')

while True:
    try:
        x = int(input("Digite 1 ou 2: "))
        while x != 1 and x != 2:
            print(f'O número "{x}" não é 1 ou 2')
            x = int(input("Digite 1 ou 2: "))
        break
    except ValueError:
        print("Digite um número inteiro válido.")

print("Você digitou 1 ou 2\n")

########################################################################

print('"not" Inverte a condição.')

while True:
    try:
        z = int(input("Digite o número 5: "))
        while not z == 5:
            print(f"O número {z} não é 5.")
            z = int(input("Digite o número 5: "))
        break
    except ValueError:
        print("Digite um número inteiro válido.")

print("Correto, você digitou 5\n")

########################################################################

print('"in" Verifica se está dentro de um conjunto/lista.')

while True:
    try:
        n2 = int(input("Digite um número diferente de 1, 2 ou 3: "))
        while n2 in (1, 2, 3):
            print(f"O número {n2} NÃO é permitido.")
            n2 = int(input("Digite um número diferente de 1, 2 ou 3: "))
        break
    except ValueError:
        print("Digite um número inteiro válido.")

print(f"O número {n2} é permitido.\n")

########################################################################

print('"not in" Verifica se NÃO está no conjunto.')

while True:
    try:
        n = int(input("Escolha 1, 2 ou 3: "))
        while n not in (1, 2, 3):
            print(f"O número {n} não está nas opções.")
            n = int(input("Escolha 1, 2 ou 3: "))
        break
    except ValueError:
        print("Digite um número inteiro válido.")

print(f"Você escolheu {n}")
########################################################################

input("\nAperte qualquer coisa para fechar...")