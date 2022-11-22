'''
Escreva um programa que leia um valor em metros 
e exiba convertido em centímetros e milímetros.
'''

while ' ':
    metro = input('Digite uma distância em metros: ').replace(',', '.')
    
    try:
        metro = float(metro)
        print(
            f'{metro/1000}km'
            f'\n{metro/100}hm'
            f'\n{metro/10}dam'
            f'\n{metro}cm'
            f'\n{metro/0.1}dm'
            f'\n{metro/0.01}cm'
            f'\n{metro/0.001}mm'
            )
        print()
    except ValueError:
        print('Digite apenas números!\n')
