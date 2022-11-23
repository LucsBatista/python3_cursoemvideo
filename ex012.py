'''
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço com 5% de desconto.
'''

while True:
    preco = input('Preço do produto: ').replace(',', '.')
    try:
        preco = float(preco)
        novo_preco = preco - (preco * 0.05)
        print(f'O produto que custa R$ {preco} com 5% de desconto custará R$ {novo_preco:.2f}\n')
    except:
        print('Digite apenas números!\n')
