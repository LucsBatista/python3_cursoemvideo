'''
Faça um programa que converta uma temperatura
digitadada em °C e converta para °F e K.
'''

while True:
    temperatura = input('• Informe a temperatura em °C: ').replace(',', '.')
    try:
        temperatura = float(temperatura)
        fahrenheit = (temperatura * 9/5) + 32
        kelvin = (temperatura + 273.15)
        print(f'A temperatura de {temperatura} °C corresponde a {fahrenheit} °F')
        print(f'A temperatura de {temperatura} °C corresponde a {kelvin} K\n')
    except:
        print('Digite apenas números!\n')