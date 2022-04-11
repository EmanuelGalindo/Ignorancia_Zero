'''
Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

valor = int(input("Informe um número inteiro: "))
if valor > 0:
    print(f"O número {valor} é positivo")
elif valor < 0:
    print(f"O número {valor} é negativo")
else:
    print("O número informado é igual a 0 (zero)")