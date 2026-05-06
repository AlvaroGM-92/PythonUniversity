print('*** Sistema de Envios ***')

# Variables que pueden ser cambiadas
tarifa_nacional = 10
tarifa_internacional = 20

# Introduccion de datos
destino = input('El envio es Nacional o Internacional? ')
peso = float(input('Introduce el peso en kilos: '))
destino_final = None
total_tasa = None

# Calculador
if destino.strip().lower() == 'nacional':
    destino_final = 'Nacional'
    total_tasa = tarifa_nacional * peso
elif destino.strip().lower() == 'internacional':
    destino_final = 'Internacional'
    total_tasa = tarifa_internacional * peso
else:
    print('No has proporcionado un destino correcto')

print(f'''\nPara el destino seleccionado se aplica tarifa: {destino_final}
Cuyo importe total sera de: ${total_tasa:.2f}''')