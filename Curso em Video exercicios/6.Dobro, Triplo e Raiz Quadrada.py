from math import trunc, sqrt

print("Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada\n")

def dtrq():
    while True:
        try:
            entry = (input("Digite um número: "))
            num = float(entry)
            RaizQ = sqrt(num)
            Trip = num * 3
            Dob = num * 2
            return num, RaizQ, Trip, Dob
        except ValueError:
            print(f'"{entry}" é inválido, digite um número.')

num, RaizQ, Trip, Dob = dtrq()    

if num.is_integer():
    print(f"""o Dobro de {trunc(num)} é {trunc(Dob)}
    o Triplo de {trunc(num)} é {trunc(Trip)}
    A Raiz Quadrada de {trunc(num)} é {RaizQ}""")
else:
    print(f"""o Dobro de {num} é {Dob}
    o Triplo de {num} é {Trip}
    A Raiz Quadrada de {num} é {RaizQ}""")

input("\nAperte qualquer coisa para fechar...")
