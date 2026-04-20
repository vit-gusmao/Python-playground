#toda memória é armazenada em um espaço do computador.
#cada memória armazenada começa no 0, não no 1.

print("Modificação de texto")

print('"string.replace(antigo, novo)" substitui partes da string.')
algo = input("Digite algo: ")
old = input("Texto que será substituído: ")
new = input("Novo texto: ")
print(f' Resultado: "{algo.replace(old, new)}"\n')

print('"string.upper()" e "string.lower()" transformam maiúsculas e minúsculas.')
algo = input("Digite algo: ")
print(f''' "{algo}" em maiúsculo: "{algo.upper()}"
"{algo}" em minúsculo: "{algo.lower()}"\n''')

print('"string.capitalize()" deixa só a primeira letra maiúscula.')
algo = input("Digite algo: ")
print(f' "{algo}" capitalizado: "{algo.capitalize()}"\n')

print('"string.title()" deixa cada palavra com inicial maiúscula.')
algo = input("Digite algo: ")
print(f' "{algo}" em title: "{algo.title()}"\n')

input("\nAperte qualquer coisa para fechar...")