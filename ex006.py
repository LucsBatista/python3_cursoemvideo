'''
Crie um programa que leia um número e
mostre seu dobro, triplo e raiz quadrada.
'''
#import math

while True:
    num = input('Digite um número: ')
    try:
        num = float(num)
        print(f'• O dobro de {num} vale {num*2}')
        print(f'• O triplo de {num} vale {num*3}')
        print(f'• A raiz quadrada de {num} vale {num**0.5:.2f}\n')
    except:
        print('Digite apenas números!\n')
