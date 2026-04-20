print("Operadores de comparação\n")
print("Eles são usados para comparar valores e sempre retornam True ou False\n")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

igual = n1 == n2
diferente = n1 != n2
maior = n1 > n2
menor = n1 < n2
maiorIgual = n1 >= n2
menorIgual = n1 <= n2

print(f"""Igual (==): {n1} == {n2} -> {igual}
Diferente (!=): {n1} != {n2} -> {diferente}
Maior que (>): {n1} > {n2} -> {maior}
Menor que (<): {n1} < {n2} -> {menor}
Maior ou igual (>=): {n1} >= {n2} -> {maiorIgual}
Menor ou igual (<=): {n1} <= {n2} -> {menorIgual}
""")

input("\nAperte qualquer coisa para fechar...")