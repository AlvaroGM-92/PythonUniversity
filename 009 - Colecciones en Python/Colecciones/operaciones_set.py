print('*** Operaciones con Set ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f'Union a | b: {union}') # Une las cadenas

interseccion = a & b
print(f'Intersection a & b: {interseccion}') # Los comunes en ambos

diferencia = a - b
print(f'Diferencia a - b: {diferencia}') # Se quitan los elementos que se repitan en el primero