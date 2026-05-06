print('*** Sistema Autenticacion ***')

USUARIO = 'admin'
PASSWORD = '123'

usuario_input = input(str('Cual es tu usuario? '))
password_input = input(str('Cual es tu password? '))

comprobacion = usuario_input.strip() == USUARIO and password_input.strip() == PASSWORD

print(f'Datos correctos? {comprobacion}')