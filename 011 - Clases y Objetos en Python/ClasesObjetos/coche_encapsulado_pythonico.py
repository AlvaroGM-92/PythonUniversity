# Definimos la clase coche
class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo publico
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo privado

    def conducir(self):
        print(f'''Conduciendo el coche:
    Marca: {self._marca}
    Modelo: {self._modelo}
    Color: {self._color}''')

    # def get_marca(self):
    #     return self._marca

    @property
    def marca(self):
        return self._marca

    # def set_marca(self, marca):
    #     self._marca = marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == "__main__":
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Toyota 2'
    coche1.modelo = 'Yaris 2'
    coche1.color = 'Azul 2'
    coche1.conducir()

    coche1.marca ='Toyota 3'
    print(f'Atributo para coche1: {coche1.marca}')
