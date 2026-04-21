print("""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.\n""")

print("O limite de velocidade do carro é 80Km/h, a multa por ultrapassar é R$7,00 por cada Km acima do limite.")
spd = float(input("Digite a velocidade em Km/h do carro: "))
multa = (spd - 80) * 7
if spd > 80.00:
    print(f"O carro foi multado. a multa será de R${spd:.2f}")
else:
    print(f"O carro não foi multado.")

input("\nAperte qualquer tecla para fechar...")