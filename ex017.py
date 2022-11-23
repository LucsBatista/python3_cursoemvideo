'''
Faça um programa que calcule a hipotenusa
'''
while True:
    co = input('• Comprimento do cateto oposto: ').replace(',', '.')
    ca = input('• Comprimento do cateto adjacente: ').replace(',', '.')
    try:
        co = float(co); ca = float(ca)
        hipotenusa = (co**2 + ca**2) ** 0.5
        print(f'A hipotenusa vai medir {hipotenusa:.2f}\n')
    except:
        print(f'Digite apenas números!\n')