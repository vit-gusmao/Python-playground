import math

import math

print("'math.sqrt(var)' = raiz quadrada.\n")
num = int(input("Digite um número: "))
print(f"A raiz quadrada de {num} é {math.sqrt(num)}\n")


print("'math.ceil(var)' arredonda para cima.\n'math.floor(var)' arredonda para baixo.\n")
num = float(input("Digite um número decimal: "))
print(f"{num} -> ceil: {math.ceil(num)} | floor: {math.floor(num)}\n")


print("'math.trunc(var)' remove a parte decimal.\n")
num = float(input("Digite um número decimal: "))
print(f"{num} truncado fica {math.trunc(num)}\n")


print("'math.pow(a, b)' = potência (a elevado a b).\n")
base = float(input("Base: "))
exp = float(input("Expoente: "))
print(f"{base}^{exp} = {math.pow(base, exp)}\n")


print("'math.factorial(var)' = fatorial.\n")
num = int(input("Digite um número inteiro: "))
print(f"Fatorial de {num} = {math.factorial(num)}\n")


print("'math.hypot(a, b)' = hipotenusa.\n")
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente: "))
print(f"Hipotenusa = {math.hypot(co, ca)}\n")


print("'math.sin / cos / tan' = seno, cosseno e tangente (usa radianos).\n")
angulo = float(input("Digite um ângulo em graus: "))
rad = math.radians(angulo)
print(f"Seno: {math.sin(rad)}")
print(f"Cosseno: {math.cos(rad)}")
print(f"Tangente: {math.tan(rad)}\n")


print("'math.radians(var)' = converte graus → radianos.\n'math.degrees(var)' = radianos → graus.\n")
ang = float(input("Digite um ângulo em graus: "))
print(f"{ang} graus em radianos = {math.radians(ang)}\n")


print("'math.log(var)' = log natural.\n'math.log10(var)' = log base 10.\n")
num = float(input("Digite um número: "))
print(f"log natural: {math.log(num)}")
print(f"log base 10: {math.log10(num)}\n")


print("'math.e' e 'math.pi' = constantes matemáticas.\n")
print(f"Valor de e = {math.e}")
print(f"Valor de pi = {math.pi}\n")