from math import pi
class Circulo:
    radio = 2

    """
    El decorador @property permite convertir cualquier metodo de una clase en
    propiedad o atributo de la misma.
    """
    @property
    def area(self):
        return '{0}'.format(pi * (self.radio ** 2))

c = Circulo()

# Sin el decorador @property se llama al metodo area correcto
#print(c.area())

# Al ser una propiedad de la clase puede llamarse sin usar parentesis
print(c.area)
