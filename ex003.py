'''
Crie um programa que leia dois números
e mostre a soma entre eles.
'''

while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    
    try:
        soma = float(num1) + float(num2)
        print(f'\n• A soma entre {num1} + {num2} = {soma}')
        cont = input('Quer continuar? [s]im: ').strip().lower()

        if cont == 's':
            print()
            continue
        else:
            print('Saindo do programa...')
            break

    except ValueError:
        print('\nOpa! Não consigo fazer essa conta. Tente novamente...')
