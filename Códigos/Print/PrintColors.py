print("Cores")

print("Códigos ANSI permitem mudar a cor do texto no terminal.\n")

print('Formato: "\\033[style;text;backgroundm\\033[m"\n')

print("""Estilos:
0 = sem estilo
1 = \033[1mnegrito\033[m
4 = \033[4msublinhado\033[m
7 = \033[7mfundo invertido\033[m\n""")

print("""Cores do texto:
30 = \033[30mpreto\033[m
31 = \033[31mvermelho\033[m
32 = \033[32mverde\033[m
33 = \033[33mamarelo\033[m
34 = \033[34mazul\033[m
35 = \033[35mroxo\033[m
36 = \033[36mciano\033[m
37 = \033[37mcinza\033[m\n""")

print("""Cores de fundo:
40 = \033[40mpreto\033[m
41 = \033[41mvermelho\033[m
42 = \033[42mverde\033[m
43 = \033[43mamarelo\033[m
44 = \033[44mazul\033[m
45 = \033[45mroxo\033[m
46 = \033[46mciano\033[m
47 = \033[47mcinza\033[m\n""")

###################################################################################

print("Máquina de fazer texto colorido\n")

algo = input("Digite algo: ")
style = input("Selecione o número do estilo: ")
while style not in ("0", "1", "4", "7"):
    print(f"o estilo {style} é inválido, escolha entre o número 0, 1, 4, 7")
    style = input("Digite o style: ")

textcolor = input("Selecione o número da cor do texto: ")
while not (textcolor.isdigit() and 30 <= int(textcolor) <= 37):
    print(f"o número {textcolor} é inválido, escolha entre 30 a 37")
    textcolor = input("Selecione o número da cor do texto: ")

textback = input("Selecione o número da cor do texto: ")
while not (textback.isdigit() and 40 <= int(textback) <= 47):
    print(f"o número {textback} é inválido, escolha entre 40 a 47")
    textcolor = input("Selecione o número da cor do texto: ")

print(f"\033[{style};{textcolor};{textback}m{algo}\033[m")

input("\nAperte qualquer coisa para fechar...")