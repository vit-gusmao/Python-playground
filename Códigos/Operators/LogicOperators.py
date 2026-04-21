# Operadores lógicos e de pertencimento com exemplos

print("Operadores lógicos e de pertencimento\n")
print("Eles são usados para combinar condições ou verificar se um valor está em uma sequência\n")

###################################################################################
print("Operador AND")

print('"and" → ambas condições precisam ser verdadeiras.\n')
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

resultado_and = (n1 > 0) and (n2 > 0)

print(f"""Resultado:
Os dois números são maiores que 0? {resultado_and}\n""")

###################################################################################
print("Operador OR")

print('"or" → pelo menos uma condição precisa ser verdadeira.\n')
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

resultado_or = (n1 > 0) or (n2 > 0)

print(f"""Resultado:
Pelo menos um número é maior que 0? {resultado_or}\n""")

###################################################################################
print("Operador NOT")

print('"not" → inverte o resultado da condição.\n')
n = int(input("Digite um número: "))

resultado_not = not (n > 0)

print(f"""Resultado:
O número NÃO é maior que 0? {resultado_not}\n""")

###################################################################################
print("Operador IN")

print('"in" → verifica se um valor está dentro de uma lista.\n')
lista = [1, 2, 3, 4, 5]

n = int(input("Digite um número para verificar na lista [1,2,3,4,5]: "))

resultado_in = n in lista

print(f"""Resultado:
O número {n} está na lista? {resultado_in}\n""")

###################################################################################
print("Operador NOT IN")

print('"not in" → verifica se um valor NÃO está dentro de uma lista.\n')
lista = [1, 2, 3, 4, 5]

n = int(input("Digite um número para verificar na lista [1,2,3,4,5]: "))

resultado_not_in = n not in lista

print(f"""Resultado:
O número {n} NÃO está na lista? {resultado_not_in}\n""")

input("Aperte qualquer coisa para fechar...")
###################################################################################
print("Operador IS")

print('"is" → verifica se duas variáveis são o MESMO objeto na memória.\n')

a = [1, 2, 3]
b = a
c = [1, 2, 3]

resultado_is1 = (a is b)
resultado_is2 = (a is c)

print(f"""Resultado:
a e b são o mesmo objeto? {resultado_is1}
a e c são o mesmo objeto? {resultado_is2}\n""")
###################################################################################
print("Operador IS NOT")

print('"is not" → verifica se duas variáveis NÃO são o mesmo objeto.\n')

a = [1, 2, 3]
b = a
c = [1, 2, 3]

resultado_is_not1 = (a is not b)
resultado_is_not2 = (a is not c)

print(f"""Resultado:
a e b NÃO são o mesmo objeto? {resultado_is_not1}
a e c NÃO são o mesmo objeto? {resultado_is_not2}\n""")