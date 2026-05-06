print('*** Sistema de Reserva de Hotel ***')

# Constantes
CON_VISTAS_MAR = 190.50
SIN_VISTAS_MAR = 150.50

# Inputs
nombre_cliente = input('Nombre del Cliente: ')
dias_estadia = int(input('Dias de estadia: '))
tiene_vistas_mar_txt = input('Con vista al mar (Si/No)? ')
tiene_vistas_mar = tiene_vistas_mar_txt.strip().lower() == 'si'

# Calculo de precio
if tiene_vistas_mar:
    precio_final = CON_VISTAS_MAR * dias_estadia
else:
    precio_final = SIN_VISTAS_MAR * dias_estadia

# Impresion por pantalla
print(f'''\n---------- Detalles de la Reservacion ----------
Cliente: {nombre_cliente}
Dias de estadia: {dias_estadia}
Costo total: {precio_final:.2f}
Habitacion con vistas al mar: {'Si' if tiene_vistas_mar else 'No'}''')