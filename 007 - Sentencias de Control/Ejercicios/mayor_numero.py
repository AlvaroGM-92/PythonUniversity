print('*** El Mayor de Dos Numeros ***')

numero1 = int(input('Escribe el primer numero: '))
numero2 = int(input('Escribe el segundo numero: '))
mayor = 0

if numero1 > numero2:
    print(f'El numero 1 es mayor: {numero1}')
elif numero1 < numero2:
    print(f'El numero 2 es mayor: {numero2}')
else:
    print(f'Los valores son iguales: Numero 1 = {numero1} y Numero 2 = {numero2}')