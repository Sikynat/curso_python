print('Conversor de temperatura')

temperatura_celsius = float(input('Digite uma temperatura em Cº: '))
print(f'A temperatura digitada foi: {temperatura_celsius}') 

calculo_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f'A conversão de Cº{temperatura_celsius} é Fº{calculo_fahrenheit}')