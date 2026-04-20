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
    print("você não escolheu 1, 2 ou 3")
    elseif = int(input("escolha 1, 2 ou 3: "))

if ifelse == 1:
    print("você escolheu 1")
elif ifelse == 2:
   print("você escolheu 2")
else:
    print("você escolheu 3")


input("\nAperte qualquer coisa para fechar...")