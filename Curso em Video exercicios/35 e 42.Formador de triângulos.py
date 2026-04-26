print("""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo e qual é o tipo do triângulo que será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes\n""")

retas = []
while True:
    retas = []
    try:
        for i in range (3):
            reta = float(input(f"Digite o valor da {i + 1}° reta: "))
            retas.append(reta)
        break    
    except ValueError:
        print("Valor inválido. Digite um número válido para as retas.")

retasfrmt = [int(reta) if reta.is_integer() else reta for reta in retas]
tri = retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]


if tri:
    print(f'As retas "{retasfrmt[0]}", "{retasfrmt[1]}" e "{retasfrmt[2]}" formam um triângulo.')
    if retasfrmt[0] == retasfrmt[1] == retasfrmt[2]:
        print("Triângulo equilátero")
    elif retasfrmt[0] == retasfrmt[1] or retasfrmt[0] == retasfrmt[2] or retasfrmt[1] == retasfrmt[2]:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print(f'As retas {retasfrmt[0]}, {retasfrmt[1]} e {retasfrmt[2]} não formam um triângulo.')

input("\nAperte qualquer tecla para fechar...")