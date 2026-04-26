print("Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.\n")

def ler_data():
    while True:
        try:
            
            dia = int(input("Dia: "))
            while dia < 1 or dia > 31:
                print(f'"{dia}" não é um dia válido.')
                dia = int(input("Dia: "))

            mes = int(input("Mes: "))
            while mes < 1 or mes > 12:
                print(f'"{mes}" não é um mês válido.')
                mes = int(input("Mês: "))

            ano = int(input("Ano: "))
            return dia, mes, ano

        except ValueError:
            print("Digite somente Números inteiros.")

dia, mes, ano = ler_data()

print(f"\nVocê nasceu em {dia:02}/{mes:02}/{ano}.")

input("\nAperte qualquer coisa para fechar...")