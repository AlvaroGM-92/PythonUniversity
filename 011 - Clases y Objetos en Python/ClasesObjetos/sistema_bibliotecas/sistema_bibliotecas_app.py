from sistema_bibliotecas.biblioteca import Biblioteca
from sistema_bibliotecas.libro import Libro

bibliotecaNacional = Biblioteca('Biblioteca Nacional')

print(f'*** Bienvenidos a la {bibliotecaNacional.nombre} ***')

# Definion de libros
libro1 = Libro('Cien años de soledad', 'Gabriel Garcia Marquez', 'Ficcion')
libro2 = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Comedia')
libro3 = Libro('El amor en los tiempos del colera', 'Gabriel Garcia Marquez', 'Ficcion')
libro4 = Libro('Pedro Paramo', 'Juan Rulfo', 'Ficcion')
libro5 = Libro('Pantaleon y las visitadoras', 'Mario Vargas Llosa', 'Comedia')

# Agregar los libros a la biblioteca
bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)

# Buscar libros por autor
autor = 'Gabriel Garcia Marquez'
print(f'\nLibros del autor: {autor}')
bibliotecaNacional.buscar_libro_autor(autor)

# Buscar libros por genero
genero = 'Ficcion'
print(f'\nLibros del genero: {genero}')
bibliotecaNacional.buscar_libro_genero(genero)

# Mostrar todos los libros
bibliotecaNacional.mostrar_todos_los_libros()
