'''
Faça um programa que leia a largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m².
'''

while True:
    largura = input('• Largura da parede: ').replace(',', '.')
    altura = input('• Altura da parede: ').replace(',', '.')
    try:
        largura = float(largura); altura = float(altura)
        area = largura * altura
        print(f'Sua parede tem dimensão de {largura}x{altura} e sua área é de {area}m².')
        print(f'Para pintar essa parede, você precisará de {area/2}l de tinta.\n')
    except TypeError:
        print('Digite apenas números!\n')
