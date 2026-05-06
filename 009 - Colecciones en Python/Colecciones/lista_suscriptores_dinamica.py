print('--- Lista de Suscriptores ---')

# Definimos el set inicial
# suscriptores = {} # Aqui se define un diccionario vacio
suscriptores = set() # Definimos un set vacio

numero_suscriptores = int(input('Proporciona el numero de suscriptores iniciales: '))
for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

print(f'Lista de suscriptores: {suscriptores}')

nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')

if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya esta en la lista: {suscriptores}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'Agregado el nuevo suscriptor: {nuevo_suscriptor}')

print(f'Lista de suscriptores: {suscriptores}')

suscriptor_eliminar = input('Proporciona el susccriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

print('--- Lista de Suscriptores ---')
for suscriptor in suscriptores:
    print(suscriptor)