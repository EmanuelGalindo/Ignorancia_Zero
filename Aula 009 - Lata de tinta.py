'''
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    - Comprar apenas latas de 18 litros;
    - Comprar apenas galões de 4 litros;
    - Misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
'''

area = int(input("Informe a área a ser pintada (em m²): "))
area = area + (area * 0.1)

demanda_tinta = area // 6
if area % 6 > 0:
    demanda_tinta += 1
print(f"Litros necessários: {demanda_tinta:.0f}")
print("")

#Apenas Latas
print("APENAS LATAS")
latas = demanda_tinta // 18
if demanda_tinta % 18 > 0:
    latas = latas + 1
preco_latas = latas * 80
print(f"Latas necessárias: {latas:.0f}")
print(f"Preço/latas: R$ {preco_latas:.2f}")

print("")

#Apenas Galões
print("APENAS GALÕES")
galoes = demanda_tinta // 4
if demanda_tinta % 4 > 0:
    galoes = galoes + 1
preco_galoes = galoes * 25
print(f"Galões necessários: {galoes:.0f}")
print(f"Preço/galoes: R$ {preco_galoes:.2f}")
print("")

#Latas e Galões (misturados) [COM ERRO]
print("LATAS E GALÕES (MISTURADOS)")
latas2 = demanda_tinta // 18
if (demanda_tinta % 18 > 0) and (demanda_tinta % 18 <= 4):
    latas2 = int(latas2)
preco_latas2 = latas2 * 80
print(f"Latas necessárias: {latas2:.0f}")
print(f"Galões necessários: 1")
print(f"TOTAL: R$ {preco_latas2 + 25:.2f}")