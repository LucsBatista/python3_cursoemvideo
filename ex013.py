'''
Faça um algoritmo que leia o salário de um funcionário
e mostreu seu novo salário com 15% de aumento.
'''

while True:
    salario = input('Salário do funcionário: ').replace(',', '.')
    try:
        salario = float(salario)
        novo_salario = salario + (salario * 0.15)
        print(f'Um funcionário que ganha R$ {salario} com 15% de aumento passa a receber R$ {novo_salario:.2f}\n')
    except:
        print('Digite apenas números!\n')
