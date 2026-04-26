from math import sqrt

print("Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada\n")

while True:
    try:
        n = float(input("Digite um número: "))
        break
    except ValueError:
        print("Digite somente números.")

num = int(n) if n.is_integer() else n

Dob = num * 2
Trip = num * 3
RaizQ = sqrt(num)

print(f"""o Dobro de {num} é {Dob}
o Triplo de {num} é {Trip}
A Raiz Quadrada de {num} é {RaizQ}""")

input("\nAperte qualquer coisa para fechar...")
