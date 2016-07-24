class Padre():
    """
    Clase padre de la cual van a heredar otras clases
    """
    nombre_padre = ""
    def __init__(self):
        print('Init del padre')

    def get_nombre_padre(self):
        return '{0}'.format(self.nombre_padre)


class PrimerHijo(Padre):
    """
    Clase hija que hereda de clase Padre, al hacer esto, cualquier instancia u
    objeto de la clase hija heredan los metodos y atributos del padre, para
    mandar a llamar o ejecutar cualquier metodo del padre usamos super()
    """
    def __init__(self, nombre):
        self.nombre = nombre
        print("Inicializador de la clase hija")
        super().__init__()


objPrimerHijo = PrimerHijo("Primer hijo")
objPrimerHijo.nombre_padre = "Nombre del padre ClassPadre"
#print(objPrimerHijo.nombre_padre)
print(objPrimerHijo.get_nombre_padre())
