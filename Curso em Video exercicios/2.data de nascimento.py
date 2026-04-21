print("Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.\n")
dia = input("Dia: ")
while dia < 0 or dia > 31:
    print(f'"{dia}" não é um dia válido.')
    dia = input("Dia: ")
mes = input("Mês: ")
while mes < 0 or mes > 12:
    print(f'"{mes}" não é um mês válido.')
ano = input("Ano: ")


print(f"Você nasceu no dia {dia} de {mes} de {ano}.")

input("\nAperte qualquer coisa para fechar...")