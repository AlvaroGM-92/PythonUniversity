print('*** Agenda de Contactos ***')

agenda = {
    'Carlos': {
        'telefono': '55667711',
        'email': 'carlos@gmail.com',
        'direccion': 'Calle Principal 132'
    },
    'Maria': {
        'telefono': '99887733',
        'email': 'maria@mail.com',
        'direccion': 'Avenida Central 456'
    },
    'Pedro': {
        'telefono': '55139078',
        'email': 'pedro@mail.com',
        'direccion': 'Plaza Mayor 789'
    }
}

print(agenda)

# Acceder a la informacion de un contacto en especifico
print(f'''Informacion del contacto de Maria
    Telefono: {agenda['Maria']['telefono']}
    Email: {agenda.get('Maria').get('email')}
    Direccion: {agenda.get('Maria').get('direccion')}
''')

# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '55678392',
    'email': 'ana@mail.com',
    'direccion': 'Calle Salvador Diaz 321'
}

print(agenda)

# Eliminar un contacto existente
agenda.pop('Pedro')
# del agenda ['Pedro']
print(agenda)

# Mostramos los contactos de la agenda
print(f'\nContactos de la agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Telefono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Direccion: {detalles.get('direccion')}
''')