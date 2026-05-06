print('*** Promedio de Calificaciones ***')

cantidad_calificaciones = int(input('Proporciona el no. de calificaciones a evaluar: '))
calificaciones = []

for calificacion in range(cantidad_calificaciones):
    calificacion = float(input(f'Calificacion {calificacion + 1}: '))
    calificaciones.append(calificacion)

print(f'\nLas calificaciones proporcionadas son: {calificaciones}')

promedio = sum(calificaciones) / cantidad_calificaciones

print(f'\nPromedio de las calificaciones: {promedio:.2f}')