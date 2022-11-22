'''
Faça um programa que leia um número inteiro
e mostre na tela seu sucessor e seu antecessor.
'''

while True:
    num = input('Núm: ')
    try:
        num = int(num)
        print(f'Analisando o valor {num}, seu antecessor é [{num-1}] e seu sucessor é [{num+1}]')
        break
    except ValueError:
        print('Digite um número inteiro!')
