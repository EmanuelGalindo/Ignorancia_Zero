'''
Faça um programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observe os termos no plural e a colocação do "e", da vírgula,
entre outros. Exemplos:
    326 = 3 centenas, 2 dezenas e 6 unidades;
    12 = 1 dezena e 2 unidades.

Teste também com: 326; 300; 100; 320; 310; 305; 301;
101; 311; 111; 25; 20; 10; 21; 11; 1; 7; e 16.
'''

import sys

numero = int(input("Informe um número inteiro menor que 1000: "))
numero_fixo = numero

if numero >= 1000:
    print("Um número maior ou igual a 1000 foi informado. Por favor, reinicie o programa e tente novamente.")
    sys.exit()
print("")

lista_centenas = []
lista_dezenas = []
lista_unidades = []

if numero - 100 >= 0:
    while numero - 100 >= 0:
        lista_centenas.append(numero)
        numero = numero - 100
contagem_centenas = len(lista_centenas)

if numero - 10 >= 0:
    while numero - 10 >= 0:
        lista_dezenas.append(numero)
        numero = numero - 10
contagem_dezenas = len(lista_dezenas)

if numero - 1 >= 0:
    while numero - 1 >= 0:
        lista_unidades.append(numero)
        numero = numero - 1
contagem_unidades = len(lista_unidades)

print(f'''Analisando o número {numero_fixo}, observa-se que o mesmo possui:
    - {contagem_centenas} centena(s);
    - {contagem_dezenas} dezena(s);
    - {contagem_unidades} unidade(s).
''')