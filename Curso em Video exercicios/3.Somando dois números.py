print("Crie um script Python que leia dois números e tente mostrar a soma entre eles.\n")

while True:
    num = []
    try:
        for i in range(2):
            n = float(input(f"Digite o {i + 1}° número: "))
            num.append(n)
        break        
    except ValueError:
        print("Digite somente números.")

numf = [int(n) if n.is_integer() else n for n in num]
soma = numf[0] + numf[1]

print(f"A soma entre {numf[0]} + {numf[1]} = {soma} ")

input("\nAperte qualquer coisa para fechar...")