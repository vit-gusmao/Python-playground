print("Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.\n")

while True:
    try:
        m = float(input("Digite o valor do seu metro: "))
        break
    except ValueError:
        print("Valor inválido. Digite um número.")

M = int(m) if m.is_integer() else m

cm = M * 100
mm = M * 1000

print(f"""{M} metros é igual a {cm} centimetros.
{M} metros é igual a {mm} milimetros.""")

input("\nAperte qualquer coisa para fechar...")