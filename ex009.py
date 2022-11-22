'''
Faça um programa que leia um número inteiro
e mostre na tela a sua tabuada (1-10).
'''

while True:
    num = input('Digite um número: ')
    try:
        num = int(num)
        for i in range(1, 11):
            print(f'{num:>5} * {i} = {num * i}')
        print()
    except ValueError:
        print('Digite apenas números inteiros!\n')
