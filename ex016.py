'''
Crie um programa que leia um número Real
e mostre apenas sua parte inteira.
Ex.: 6.324 -> 6
'''

while True:
    num = input('Digite um número: ').replace(',', '.')
    try:
        num = float(num)
        print(int(num))
    except:
        print('Digite apenas números!\n')