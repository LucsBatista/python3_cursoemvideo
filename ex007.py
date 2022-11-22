'''
Crie um programa que leia as duas notas de 
um aluno, calcule e mostre sua média artmética
'''

while 1:
    nota1 = input('Digite a 1º nota: ').replace(',', '.')
    nota2 = input('Digite a 2º nota: ').replace(',', '.')
    
    try:
        media = (float(nota1) + float(nota2)) / 2
        print(f'A média desse aluno é igual a {media:.1f}\n')
    except ValueError:
        print('Digite apenas números!\n')
