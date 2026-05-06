print('*** Sistema de Autenticacion ***')

# Constantes
USUARIO = 'Admin'
PASSWORD = 'Contraseña123'

# Peticion de datos
usuario = input('Introduce usuario: ')
password = input('Introduce password: ')

# Comprobaciones
if USUARIO == usuario and PASSWORD == password:
    print('Bienvenido al sistema')
elif USUARIO == usuario:
    print('Password incorrecto')
elif PASSWORD == password:
    print('Usuario incorrecto')
else:
    print('Usuario y Password incorrectos')