print("""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média de suas notas, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0:
Reprovado

- Média entre 5.0 e 6.9:
Recuperação

- Média 7.0 ou superior:
Aprovado\n""")


nome = input("Digite o nome do aluno: ").strip()
while not nome.replace(" ", "").isalpha():
    print(f'Nomes possui somente letras.')
    nome = input("Digite seu nome: ").strip()

while True:
    try:
        n1 = float(input("Digite uma nota: "))
        n2 = float(input("Digite outra nota: "))
        media = (n1 + n2) / 2
        break
    except ValueError:    
        print("Digite somente números.")


if media < 5:

    status = "reprovado"

elif media <= 6.9:

    status = "em recuperação"

else:
    status = "aprovado"

media_formatada = int(media) if n1.is_integer() and n2.is_integer() else media

# Print final
print(f"""A média das notas do aluno {nome} é {media_formatada}.
{nome} está {status}.""")

input("\nAperte qualquer coisa para fechar...")