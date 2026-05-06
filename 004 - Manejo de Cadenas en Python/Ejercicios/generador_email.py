# Titulo
print('*** Generador de Email ***')

# Variables
nombre_completo = ' Alvaro Garcia Mon '
print(f'Nombre completo: {nombre_completo}')
empresa = 'Casa de Alvaro'
print(f'Empresa: {empresa}')
dominio = '.com.es'
print(f'Dominio: {dominio}')
print()

# Normalización de variables
nombre_normalizado = nombre_completo.strip().replace(' ','.').lower()
print(f'Nombre normalizado: {nombre_normalizado}')
empresa_normalizada = empresa.strip().replace(' ','').lower()
dominio_normalizado = f'@{empresa_normalizada}{dominio}'
print(f'Dominio normailzado: {dominio_normalizado}')

# Correo final
email = nombre_normalizado + dominio_normalizado
print(f'\nEl correo generado será el siguiente: {email}')