print("Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.\n")

print("O preço da passagem para viagens de até 200Km é R$0,50 por Km e mais de 200Km é R$0,45 por Km")
while True:
    try:
        dist = float(input("Qual a distância da viagem em Km: "))
        break
    except ValueError:
        print("Número inválido.")

price50 = dist * 0.50
price45 = dist * 0.45
if dist > 200.00:
    print(f"o preço da viagem será de R${price45:.2f}")
else:
    print(f"o preço da viagem será de R${price50:.2f}")

input("\nAperte qualquer tecla para fechar...")