from random import randint

print('*** Sistema Generador de ID Unico ***')

nombre = input('Cual es tu nombre? ')
apellido = input('Cual es tu apellido? ')
anyo = input('Cual es tu año de nacimiento (YYYY)? ')

# Normalizar los valores
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anyo_2 = anyo.strip()[2:] # Si no hay indice final, recupera hasta último caracter con valor

# Generar valor aleatorio
aleatorio = randint(1000, 9999)

# Generamos el ID Unico
id_unico = f'{nombre_2}{apellido_2}{anyo_2}{aleatorio}'

# Imprimir mensaje
print(f'''\nHola {nombre},
    Tu numero de identificacion (ID) generado por el sistema es:
    {id_unico}
    Felicidades!!''')

print(f'\nHola {nombre},')
print('\tTu numero de indentificacion (ID) generado por el sistema es:')
print(f'\t{id_unico}')
print('\tFelicidades!')
