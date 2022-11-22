'''
Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.
'''

texto = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(texto)}'
    f'\n\n• Tem letras-números? {texto.isalnum()}'
    f'\n• Tem somente letras? {texto.isalpha()}'
    f'\n• Tem apenas digitos? {texto.isdigit()}'
    f'\n• Tem somente espaços? {texto.isspace()}'
    f'\n• Tem caracteres ASCII? {texto.isascii()}'
    f'\n• Tem cada letra inicial em maiúsculo? {texto.istitle()}'
    f'\n\n• Está tudo em minúsculo? {texto.islower()}'
    f'\n• Está tudo em maiúsculo? {texto.isupper()}'
    f'\n• Os caracteres são decimais? {texto.isdecimal()}'
)
