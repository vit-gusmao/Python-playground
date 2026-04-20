print("Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada\n")
num = int(input("Digite um número: "))
RaizQ = num ** 2
Trip = num * 3
Dob = num * 2

print(f"""o Dobro de {num} é {Dob}
o Triplo de {num} é {Trip}
A Raiz Quadrada de {num} é {RaizQ}""")

input("\nAperte qualquer coisa para fechar...")
