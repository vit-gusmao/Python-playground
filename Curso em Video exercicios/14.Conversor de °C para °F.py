print("Faça um conversor de temperatura de Celsius para Fahrenheit.\n")

while True:
    try:
        c = float(input("Digite a temperatura em Celsius: "))
        break
    except ValueError:
        print("Valor inválido.")

C = int(c) if c.is_integer() else c
toF = (C * 1.8) + 32
print(f"{C}°C equivale a {toF:.2f}°F")

input("\nAperte qualquer coisa para fechar...")