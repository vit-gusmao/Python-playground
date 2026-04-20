#no python, é possivel importar bibliotecas que tem comandos especificos.

#"import" importa uma biblioteca inteira
import math

num = int(input("Digite um número: "))
print(f"A raiz quadrada de {num} é {math.sqrt(num)}\n")

#"from import" importa algo especifico de uma biblioteca
from random import random
aleatorio = random.random()
print(f" gerando um número aleatório agora: {aleatorio}")

input("\nAperte qualquer coisa para fechar...")