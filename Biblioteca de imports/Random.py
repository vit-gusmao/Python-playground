import random

print("'random.randint(a, b)' = número inteiro aleatório entre a e b.\n")
print(f"Número aleatório: {random.randint(1, 10)}\n")


print("'random.random()' = número aleatório entre 0 e 1.\n")
print(f"Número aleatório: {random.random()}\n")


print("'random.uniform(a, b)' = número decimal aleatório entre a e b.\n")
print(f"Número aleatório: {random.uniform(1, 10)}\n")


print("'random.choice(lista)' = escolhe um item aleatório de uma lista.\n")
lista = ["vitor", "joao", "maria", "ana"]
print(f"Escolhido: {random.choice(lista)}\n")


print("'random.shuffle(lista)' = embaralha uma lista.\n")
lista2 = [1, 2, 3, 4, 5]
random.shuffle(lista2)
print(f"Lista embaralhada: {lista2}\n")


print("'random.sample(lista, k)' = pega k itens aleatórios da lista.\n")
lista3 = [10, 20, 30, 40, 50]
print(f"Sorteados: {random.sample(lista3, 3)}\n")