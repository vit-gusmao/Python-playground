# Arrays (listas) armazenam vários valores.

print('"Arrays (listas)" armazenam vários valores.\n')

lista = []

quantidade = int(input("Digite quantos valores deseja adicionar: "))

while quantidade <= 0:
    print(f"{quantidade} é inválido. Digite um número maior que 0.")
    quantidade = int(input("Digite quantos valores deseja adicionar: "))

for i in range(quantidade):
    valor = int(input(f"Digite o {i+1}º valor: "))
    lista.append(valor)

print(f"\nLista completa: {lista}\n")

#############################################################################

print('Acessando elementos da lista.\n')

print(f"Primeiro elemento: {lista[0]}")
print(f"Último elemento: {lista[-1]}\n")

#############################################################################

print('Percorrendo lista com for.\n')

for item in lista:
    print(f"Valor: {item}")

print("Fim da lista.\n")

#############################################################################

print('Verificando se valor está na lista.\n')

buscar = int(input("Digite um valor para buscar: "))

if buscar in lista:
    print(f"{buscar} está na lista.\n")
else:
    print(f"{buscar} NÃO está na lista.\n")

#############################################################################

input("Aperte qualquer coisa para fechar...")