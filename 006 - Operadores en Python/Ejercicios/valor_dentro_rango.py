print('*** Valor dentro de Rango ***')

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

numero = int(input(f'Introduce un valor entre {VALOR_MINIMO} y {VALOR_MAXIMO}: '))

# comprobar = numero >= VALOR_MINIMO and numero <= VALOR_MAXIMO // Ambas sirven
comprobar = VALOR_MINIMO <= numero <= VALOR_MAXIMO

print(f'El valor {numero} introducido es: {comprobar}')