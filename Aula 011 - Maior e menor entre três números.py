'''
Faça um programa que leia três números e mostre o maior e o menor deles.
'''

num1 = int(input("Informe o 1º número inteiro: "))
num2 = int(input("Informe o 2º número inteiro: "))
num3 = int(input("Informe o 3º número inteiro: "))
print("")

if (num1 > num2) and (num1 > num3):
    print(f"Maior número: {num1}")

elif (num1 > num2) and (num1 == num3):
    print(f"Maior número: {num1}")

elif (num1 == num2) and (num1 > num3):
    print(f"Maior número: {num1}")

elif (num2 > 1) and (num2 > num3):
    print(f"Maior número: {num2}")

elif (num2 > 1) and (num2 > num3):
    print(f"Maior número: {num2}")

elif (num2 > 1) and (num2 == num3):
    print(f"Maior número: {num2}")

else:
    print(f"Maior número: {num3}")