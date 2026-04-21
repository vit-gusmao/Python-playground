print("""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média de suas notas, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0:
Reprovado

- Média entre 5.0 e 6.9:
Recuperação

- Média 7.0 ou superior:
Aprovado\n""")

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite uma nota: "))
n2 = float(input("Digite outra nota: "))
media = (n1 + n2) / 2

if media < 5.0:
    print(f"A média das notas do aluno {nome} é {media}. {nome} está reprovado.")

elif media >= 5.0 or media <= 6.9:
    print(f"A média das notas do aluno {nome} é {media}. {nome} está em recuperação.")

else:
    print(f"A média das notas do aluno {nome} é {media}. {nome} está aprovado.")

input("\nAperte qualquer coisa para fechar...")