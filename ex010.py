'''
Crie um programa que converta Real em Dólar
Considere US$ 1,00 = R$ 3,27
'''

while True:
    real = input('Digite um valor: R$ ').replace(',', '.')

    try:
        real = float(real)
        print(f'R$ {real:.2f} = US$ {real/3.27:.2f}')
        print()
    except:
        print('Digite apenas números!\n')
