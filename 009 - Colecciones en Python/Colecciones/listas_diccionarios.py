print('*** Listas con Diccionarios ***')

mi_lista = [
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 32
    }
]

print(mi_lista)

print('--- Lista de Nombre, Apelido y Edad ---')
for usuario in mi_lista:
    print(f'''Usuario:
    Nombre: {usuario.get('nombre')}
    Apellido: {usuario.get('apellido')}
    Edad: {usuario.get('edad')}''')