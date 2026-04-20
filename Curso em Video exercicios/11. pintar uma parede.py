print("Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².\n")

larg = float(input("Digite a largura da parede em metros: "))
alt = float(input("Digite a altura da parede em metros: "))
area = larg * alt
tinta = area / 2

print(f"""A área da parede é: {area:.2f}m²
Você vai precisar de {tinta:.2f} litros de tinta""")

input("\nAperte qualquer coisa para fechar...")