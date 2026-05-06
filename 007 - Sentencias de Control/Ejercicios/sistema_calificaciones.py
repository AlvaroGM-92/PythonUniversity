print('*** Sistema de Calificaciones ***')

nota = float(input('Proporciona una calificacion entre 0 y 10: '))
calificacion = None

# Revisar la variable con los rangos
if 10 >= nota >= 9:
    calificacion = 'A'
elif 9 > nota >= 8:
    calificacion = 'B'
elif 8 > nota >= 7:
    calificacion = 'C'
elif 7 > nota >= 6:
    calificacion = 'D'
elif 6 > nota >= 0:
    calificacion = 'F'
else:
    calificacion = 'Valor Desconocido'

# Imprimir resultado
print(f'\nCon una nota de {nota:.2f}, tu calificacion es de: {calificacion}')