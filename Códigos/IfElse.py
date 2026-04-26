print('''"if else" são usados para tomar decisões no programa
o "if" verifica uma condição
o "else" executa quando a condição do "if" é falsa
"elif" é usado para adicionar mais condições ao "if else".
A ordem sempre é:
1. if
2. elif
3. else\n''')

while True:
    try:
        ifelse = int(input("escolha 1, 2 ou 3: "))

        while ifelse not in (1, 2, 3):
            print(f"O número {ifelse} não é 1, 2 ou 3")
            ifelse = int(input("escolha 1, 2 ou 3: "))

        if ifelse == 1:
            print("você escolheu 1")
        elif ifelse == 2:
            print("você escolheu 2")
        else:
            print("você escolheu 3")
            break
    except ValueError:
        print("Digite somente 1, 2 ou 3")

#########################################################################
print('"if aninhado" verifica uma condição principal e, só se ela for verdadeira, verificar outra condição mais específica dentro dela.\n')

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Digite uma idade válida (número inteiro).")

if idade >= 18:
    print("Você é maior de idade")

    if idade >= 60:
        print("E também é idoso")
    else:
        print("E não é idoso")

else:
    print("Você é menor de idade")

########################################################################

print('\n"or" Apenas uma condição precisa ser verdadeira.')
while True:
    try:
        x = int(input("Digite 1 ou 2: "))
        while x not in (1, 2):
            print(f"O número {x} não é 1 ou 2")
            x = int(input("Digite 1 ou 2: "))
        break
    except ValueError:
        print("Digite somente 1 ou 2.")

if x == 1 or x == 2:
    print("Você digitou 1 ou 2")

##########################################################################

print('\n"and" Duas condições precisam ser verdadeiras.')
while True:
    try:
        y = int(input("\nDigite um número entre 1 e 10: "))
        while not (1 <= y <= 10):
            print(f"O número {y} não está entre 1 e 10")
            y = int(input("Digite um número entre 1 e 10: "))
        break
    except ValueError:
        print("Digite somente números entre 1 e 10.")

if y >= 1 and y <= 10:
    print(f"Você digitou {y}")

print('\n"not" Inverte a condição.')
while True:
    try:
        z = int(input("Digite o número 5: "))
        while z != 5:
            print(f"O número {z} não é 5.")
            z = int(input("Digite o número 5: "))
        break
    except ValueError:
        print("Digite somente o número 5.")

if not(z != 5):
    print("Correto, você digitou 5")

#######################################################################

print('\n"in"  Verifica se um valor está dentro de um conjunto/lista.')
while True:
    try:
        n = int(input("Escolha 1, 2 ou 3: "))
        while n not in (1, 2, 3):
            print(f"O número {n} não está nas opções de escolher.")
            n = int(input("Escolha 1, 2 ou 3: "))
        break
    except ValueError:
        print("Digite somente 1, 2 ou 3.")

if n in (1, 2, 3):
    print(f"Você escolheu {n}")

########################################################################

print('"not in" Verifica se NÃO está no conjunto/lista..')
while True:
    try:
        n2 = int(input("Digite um número diferente de 1, 2 ou 3: "))
        while n2 in (1, 2, 3):
            print(f"O número {n2} NÃO é permitido digitar.")
            n2 = int(input("Digite um número diferente de 1, 2 ou 3: "))
        break
    except ValueError:
        print("Digite somente um número diferente de 1, 2 ou 3.")

if n2 not in (1, 2, 3):
    print(f"O número {n2} é permitido digitar.")

########################################################################

print('if else inline sendo declarado na variavel')

num = []
while True:
    try:
        num = []
        for i in range(2):
            n = float(input(f"Digite o {i + 1}° número: "))
            num.append(n)
        break
    except ValueError:    
        print("Digite somente números.")




numf = [int(n) if n.is_integer() else n for n in num]
media = (numf[0] + numf[1]) / 2
mediaf = int(media) if numf[0].is_integer() and numf[1].is_integer() else media


print(f"A média dos valores {numf[0]} e {numf[1]} é {mediaf}.")

input("\nAperte qualquer coisa para fechar...") 