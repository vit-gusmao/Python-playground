print("Crie um script Python que leia dois números e tente mostrar a soma entre eles.\n")

def ler_num():
    while True:
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            soma = n1 + n2

            return n1, n2, soma

        except ValueError:
            print("Digite somente números.")

n1, n2, soma = ler_num()

print(f"A soma entre {n1} e {n2} é: {soma}")

input("\nAperte qualquer coisa para fechar...")