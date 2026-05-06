print('*** Estaciones segun numero entero ***')

numero_estacion = int(input('Introduce un numero para la estacion entre 1 y 12: '))

if numero_estacion == 1 or numero_estacion == 2 or numero_estacion == 3:
    print(f'El numero {numero_estacion} corresponde a la estacion: Invierno')
elif numero_estacion == 4 or numero_estacion == 5 or numero_estacion == 6:
    print(f'El numero {numero_estacion} corresponde a la estacion: Primavera')
elif numero_estacion == 7 or numero_estacion == 8 or numero_estacion == 9:
    print(f'El numero {numero_estacion} corresponde a la estacion: Verano')
elif numero_estacion == 10 or numero_estacion == 11 or numero_estacion == 12:
    print(f'El numero {numero_estacion} corresponde a la estacion: Otoño')
else:
    print('Numero desconocido para estacion')