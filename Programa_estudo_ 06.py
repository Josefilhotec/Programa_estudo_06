# Programa ler a largura e a altura de uma parede em metros,
# e calcula a sua Area e a quantidade de tinta necessaria para pinta-la,
# sabendo que cada litro de tinta pinta uma área de 2m².

print('# Exemplo 01')

larg = float(input(' Digite a largura: '))
alt = float(input(' Digite a altura: '))
area = larg * alt
print('''A largura sendo {} e a altura sendo {},
 sua area será {} a quantidade de tinta será {}'''.format(larg, alt, area, area / 2))

print('# Exemplo 02')

larg = float(input(' Digite a largura: '))
alt = float(input(' Digite a altura: '))
area = larg * alt
tinta = area / 2
print(' Largura:', larg, 'Altura:', alt, 'Area:', area, 'A quantidade de tinta será:', tinta)
