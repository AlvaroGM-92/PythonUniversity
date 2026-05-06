print('*** Manejo de Tuplas ***')

mi_tupla = (1, 2, 3, 4, 5)

print(mi_tupla)
# No se puede modificar una tupla
# mi_tupla[0] = 10
# mi_tupla.append(6)

# Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento, end=' ')

# Crear una tupla para una coordenada x, y
coordenadas = (3, 5)
# Accedemos a los elementos de la tupla
print(f'\nCoordenada en el eje X: {coordenadas[0]}')
print(f'Coordenada en el eje Y: {coordenadas[1]}')

# Crear una tupla unitaria
tupla_un_elemento = 10, # Hay que poner la ',' para que sea una tupla unitaria
print(f'\nTupla de un elemento: {tupla_un_elemento}')

# Tupla anidada
tuplas_anidadas = (1, (2, 3), (4, 5))
print(f'Segundo elemento de la tupla anidad: {tuplas_anidadas[1]}')