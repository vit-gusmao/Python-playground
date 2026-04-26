from random import randint

print("Crie um programa que faça o computador jogar Jokenpô com você.\n")

options = [
    "Pedra",
    "Papel",
    "Tesoura",
]

for i, option in enumerate(options, start = 1):
        print(f"Aperte {i} para escolher: {option}")

print()

while True:
    try:
       select = int(input("Selecione uma das opções: "))
       while select < 0 or select > 3:
        print("Opção inválida.")
        select = int(input("Selecione uma das opções: "))
       break
    except ValueError:
        print("Opção inválida.")

bot = randint(1,3)        

casos = [
    "Pedra empata com Pedra",
    "Papel empata com Papel",
    "Tesoura empata com Tesoura",
    "Pedra vence Tesoura",
    "Tesoura vence Papel",
    "Papel vence Pedra",
]

win = [
    "Eu venci",
    "Você venceu",
    "Empatamos"
]

resultado = ""
vencedor = 0  

for i, frase in enumerate(casos):
    palavras = frase.split()

    a = palavras[0]      
    b = palavras[-1]     

    p = options.index(a) + 1
    c = options.index(b) + 1

    if (p == select and c == bot) or (p == bot and c == select):
        resultado = frase

        vencedor = (
           2 * int("empata" in frase) +
           1 * int("vence" in frase and select == p)
        )
        break

win = win[vencedor]


print()

print(f"""Você escolheu {options[select - 1]},
Eu escolhi {options[bot - 1]},
{resultado},
{win}.""")

input("\n Aperte qualquer coisa para fechar...")