print("Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.\n")

m = int(input("Digite o valor do seu metro: "))
cm = m*100
mm = m*1000

print(f"""{m} metros é igual a {cm} centimetros.
{m} metros é igual a {mm} milimetros.""")

input("\nAperte qualquer coisa para fechar...")