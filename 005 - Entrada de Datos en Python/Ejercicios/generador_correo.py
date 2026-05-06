# Generador de correo de empresa
print('*** Sistema Generador de Email ***')

# Introduccion variables
nombre = input('Introduce tu nombre completo: ')
apellidos = input('Introduce tus apellidos: ')
nombre_empresa = input('Introduce el nombre de tu empresa: ')
extension_dominio = input('Introduce el dominio: ')

# Normalizar variables
nombre_2 = nombre.strip().lower().replace(' ', '.')
apellidos_2 = apellidos.strip().lower().replace(' ', '.')
nombre_empresa_2 = nombre_empresa.strip().lower().replace(' ', '')
extension_dominio_2 = extension_dominio.strip().lower().replace(' ', '')

# General el Email
email = f'{nombre_2}.{apellidos_2}@{nombre_empresa_2}{extension_dominio_2}'

print(f'''
Felicidades por ingresar {nombre}
    Tu correo de empresa es el siguiente:
    {email}
    Estamos encantados de tenerte aquí.''')