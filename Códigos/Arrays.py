# Arrays (listas) armazenam vários valores.

print('"Arrays (listas)" armazenam vários valores.\n')

lista = []

while True:
    try:
        quantidade = int(input("Digite quantos valores deseja adicionar: "))
        if quantidade <= 0:
            print(f"{quantidade} é inválido. Digite um número maior que 0.")
            continue
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")

for i in range(quantidade):
    while True:
        try:
            valor = int(input(f"Digite o {i+1}º valor: "))
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")
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

while True:
    try:
        buscar = int(input("Digite um valor para buscar: "))
        break
    except ValueError:
        print("Valor inválido. Digite um número inteiro válido.")

if buscar in lista:
    print(f"{buscar} está na lista.\n")
else:
    print(f"{buscar} NÃO está na lista.\n")

#############################################################################

print('Verificando o maior e menor valor da lista usando max() e min().\n')

maior = max(lista)
menor = min(lista)

print(f"O maior valor da lista é {maior}.")
print(f"O menor valor da lista é {menor}.\n")


input("Aperte qualquer coisa para fechar...")
