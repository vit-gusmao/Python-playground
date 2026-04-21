print('''"if else" são usados para tomar decisões no programa
o "if" verifica uma condição
o "else" executa quando a condição do "if" é falsa
"elif" é usado para adicionar mais condições ao "if else".
A ordem sempre é:
1. if
2. elif
3. else\n''')

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

#########################################################################

print('\n"or" Apenas uma condição precisa ser verdadeira.')
x = int(input("Digite 1 ou 2: "))
while x not in (1, 2):
    print(f"O número {x} não é 1 ou 2")
    x = int(input("Digite 1 ou 2: "))

if x == 1 or x == 2:
    print("Você digitou 1 ou 2")

##########################################################################

print('\n"and" Duas condições precisam ser verdadeiras.')
y = int(input("\nDigite um número entre 1 e 10: "))
while not (1 <= y <= 10):
    print(f"O número {y} não está entre 1 e 10")
    y = int(input("Digite um número entre 1 e 10: "))

if y >= 1 and y <= 10:
    print(f"Você digitou {y}")

print('\n"not" Inverte a condição.')
z = int(input("Digite o número 5: "))
while z != 5:
    print(f"O número {z} não é 5.")
    z = int(input("Digite o número 5: "))

if not(z != 5):
    print("Correto, você digitou 5")

#######################################################################

print('\n"in"  Verifica se um valor está dentro de um conjunto/lista.')
n = int(input("Escolha 1, 2 ou 3: "))
while n not in (1, 2, 3):
    print(f"O número {n} não está nas opções de escolher.")
    n = int(input("Escolha 1, 2 ou 3: "))

if n in (1, 2, 3):
    print(f"Você escolheu {n}")

########################################################################

print('"not in" Verifica se NÃO está no conjunto/lista..')
n2 = int(input("Digite um número diferente de 1, 2 ou 3: "))
while n2 in (1, 2, 3):
    print(f"O número {n2} NÃO é permitido digitar.")
    n2 = int(input("Digite um número diferente de 1, 2 ou 3: "))

if n2 not in (1, 2, 3):
    print(f"O número {n2} é permitido digitar.")

input("\nAperte qualquer coisa para fechar...")