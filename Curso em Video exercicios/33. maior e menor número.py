print("Faça um programa que leia três números e mostre qual é o maior e qual é o menor número.")

nums = []
while True:
    try:
        for i in range(3):
            n = float(input(f"Digite o {i + 1}° número: "))
            nums.append(n)
        break
    except ValueError:
        print("Digite apenas números.")
        
maior = max(nums)
menor = min(nums)

print(f"o maior valor digitado é: {maior}")
print(f"o menor valor digitado é: {menor}")

input("\nAperte qualquer tecla para fechar...")