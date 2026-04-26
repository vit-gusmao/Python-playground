print("Faça um programa que leia algo pelo teclado e mostre informações sobre ele.\n")

algo = input("Digite algo: ")

tipos = [

    ("string", str),
    ("inteiro", int),
    ("float", float),
    ("booleano", bool)
]

for nome, tipo in tipos:
    if type(algo) == tipo:
        print(f"É uma {nome}")
    else:
        print(f"Não é uma {nome}")

print()  


verificacoes = [
    ("É numérico", algo.isnumeric()),
    ("É alfabético (só letras)", algo.isalpha()),
    ("É alfanumérico (letras e/ou números)", algo.isalnum()),
    ("Está em MAIÚSCULAS", algo.isupper()),
    ("Está em minúsculas", algo.islower()),
    ("Está em formato de título", algo.istitle())
]

for texto, resultado in verificacoes:
    if resultado:
        print(texto)
    else:
        print(f"Não: {texto.lower()}")

input("\nAperte qualquer coisa para fechar...")

