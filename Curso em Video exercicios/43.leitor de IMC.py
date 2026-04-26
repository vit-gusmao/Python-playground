print("""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida
\n""")

nome = input("Digite seu nome: ").strip().title()
while not nome.replace(" ", "").isalpha():
    print("Nomes possui somente letras.")
    nome = input("Digite seu nome: ").strip().title()

while True:
    try:
        kg = float(input("Digite seu peso em Kg: "))
        alt = float(input("Digite sua altura em metros: "))
        break
    except ValueError:
        print("Não digite letras e simbólos.")
      

Kg = int(kg) if kg.is_integer() else kg
A = int(alt) if alt.is_integer() else alt

IMC = Kg / (alt ** 2)

verify = [
    ("Abaixo do Peso", IMC < 18.5),
    ("Peso Ideal", 18.5 <= IMC < 25),
    ("Sobrepeso", 25 <= IMC < 30),
    ("Obesidade", 30 <= IMC < 40),
    ("Obesidade mórbida", IMC >= 40)
    ]

for status, condition in verify:
    if condition:
        print(f"Seu nome é {nome}, seu peso é {Kg}kg, sua altura é {A}m, seu IMC é {IMC:.1f} e sua categoria é {status}")

input("\nAperte qualquer coisa para fechar...")
