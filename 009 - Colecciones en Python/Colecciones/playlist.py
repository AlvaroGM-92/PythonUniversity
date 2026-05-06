print('*** PLaylist de Canciones ***')

# Creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones desea agregar? '))

# iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# Empezamos a agregar canciones
# lista_reproduccion.append('Hotel California - Eagles')
# lista_reproduccion.append('Staying Alive - Bee Gees')
# lista_reproduccion.append('Dream On - Aerosmith')

# Ordenar lista en prden alfabetico. sort
lista_reproduccion.sort()

# Alfabetico inverso
# lista_reproduccion.sort(reverse=True)

# Mostrar lista de canciones
# print(f'\n Lista de Reproduccion en orden alfabetico')
# print(lista_reproduccion)

# Mostrar la lista iterando sus elementos
print('\nIteramos el Playlist')
for cancion in lista_reproduccion:
    print(f'- {cancion}')