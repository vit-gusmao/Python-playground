import random

print('''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
o programa deverá escrever na tela se o usuário venceu o perdeu\n''')

n1 = random.randint(0,5)
n2 = int(input("pensei em um número de 0 a 5, me diga qual eu escolhi: "))

while n2 < 0 or n2 > 5:
    print("você não digitou um número de 0 a 5")
    n2 = int(input("pensei em um número de 0 a 5, me diga qual eu escolhi: "))

    if n1 == n2:
        print(f"parabéns, você acertou! o número que eu pensei foi {n2}")
    else:
        print(f"você errou, o número que eu pensei foi {n2}")

    input("\nAperte qualquer coisa para fechar...")