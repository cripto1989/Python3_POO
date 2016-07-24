class Padre():
    """
    Clase padre de la cual van a heredar otras clases
    """
    nombre_padre = ""
    def __init__(self):
        print('Init del padre')

    def get_nombre_padre(self):
        return '{0}'.format(self.nombre_padre)

    def funcion_ejemplo_super(self):
        print('{0}'.format('Llamado desde super'))

class PrimerHijo(Padre):
    """
    Clase hija que hereda de clase Padre, al hacer esto, cualquier instancia u
    objeto de la clase hija heredan los metodos y atributos del padre, para
    mandar a llamar o ejecutar cualquier metodo del padre directamente usamos
    super()
    """
    def __init__(self, nombre):
        self.nombre = nombre
        print("Inicializador de la clase hija")
        # Para ejecutar un metodo directamente del padre usamos super() e
        # indicamos el nombre del metodo a usar
        super().__init__()
        super().funcion_ejemplo_super()

# Creamos una instancia de la clase hija, si la clase hija no tiene metodo Init
# se ejecuta directamente el init del padre.
objPrimerHijo = PrimerHijo("Primer hijo")

# En este ejemplo el atributo nombre_padre pertenece a la clase padre, no a la
# clase hija, al ser aplicada la herencia la instancia de la clase hija hereda
# los atributos de padre por lo tanto se puede mandar a almacenar el valor al
# atributo de padre
objPrimerHijo.nombre_padre = "Nombre del padre ClassPadre"
# imprimimos directamente el atributo heredado
#print(objPrimerHijo.nombre_padre)

#Asi mismo podemos mandar a ejecutar metodos del padre usando la instancia
print(objPrimerHijo.get_nombre_padre())
