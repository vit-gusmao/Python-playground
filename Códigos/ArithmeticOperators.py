n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divisaoInteira = n1 // n2
divisaoResto = n1 % n2

print(f"""Adição:{n1} + {n2} = {adicao}
Subtração (+):{n1} - {n2} = {subtracao}
Multiplicação (-):{n1} * {n2} = {multiplicacao}
Divisão (/):{n1} / {n2} = {divisao}
Potencia (**):{n1} ** {n2} = {potencia}
Divisão Inteira (//):{n1} // {n2} = {divisaoInteira}
Resto da divisão (%):{n1} % {n2} = {divisaoResto}\n""")

print("Ordem de Precedência: (), **, * / // %,  + -")

input("\nAperte qualquer coisa para fechar...")