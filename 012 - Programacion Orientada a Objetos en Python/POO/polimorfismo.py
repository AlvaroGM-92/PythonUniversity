# Polimorfismo
class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

# Funcion polimorfica
def hacer_sonido_animal(animal): # duck typing
    animal.hacer_sonido()

print('*** Ejemplo Polimorfismo ***')
print('Clase padre Animal')
animal1 = Animal()
animal1.hacer_sonido()
hacer_sonido_animal(animal1)

# Definimos un objeto de la clase Perro
print('\nClase hija Perro')
perro1 = Perro()
perro1.hacer_sonido()
hacer_sonido_animal(perro1)

# Definimos un objeto de la clase Gato
print('\nClase hija Gato')
gato1 = Gato()
gato1.hacer_sonido()
hacer_sonido_animal(gato1)