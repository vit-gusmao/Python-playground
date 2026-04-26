print("Faça um programa que leia um ano qualquer e mostre se ele é Bissexto")

while True:
    try:
        ano = float(input("Digite um ano qualquer: "))
        if not ano.is_integer():
            print("Digite apenas números inteiros para o ano.")
            continue
        ano = int(ano)
        break
    except ValueError:
        print("Valor inválido. Tente novamente.")

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} NÃO é bissexto")

input("\nAperte qualquer tecla para sair...")