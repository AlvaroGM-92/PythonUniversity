print('*** Sistema de Inventarios ***')

inventario = []

cantidad_inventario = int(input('Cuantos productos desea agregar al inventario? '))
for contador in range(cantidad_inventario):
    print(f'Proporciona los valores del producto {contador + 1}')
    id = contador + 1
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    inventario.append({'id': id, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad})

print()
print(inventario)
print()

id_busqueda = int(input('Ingresa el ID del producto a buscar: '))

for producto in inventario:
    if producto['id'] == id_busqueda:
        print(f'''ID: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: {producto.get('precio')}
    Cantidad: {producto.get('cantidad')}
''')

print('\n--- Inventario actuallizado ---')
for producto in inventario:
    print(f'''ID: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: {producto.get('precio')}
    Cantidad: {producto.get('cantidad')}
''')