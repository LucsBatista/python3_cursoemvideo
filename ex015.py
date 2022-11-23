''''
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa
R$ 60,00 por dia e R$ 0,15 por Km rodado.
'''

while True:
    dias_alugados = input('Quantos dias alugados? ')
    km_rodados = input('Quantos Km rodados? ')
    try:
        dias_alugados = int(dias_alugados); km_rodados = float(km_rodados)
        total = (dias_alugados * 60) + (km_rodados * 0.15)
        print(f'O total a pagar é R$ {total:.2f}\n')
    except:
        print('Digite apenas números!\n')

