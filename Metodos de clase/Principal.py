class MiClase:
    pass

    """
    Los metodos de clase hacen uso del decorador classmethod, asi como tambien
    se usa cls en lugar de self
    """
    @classmethod
    def metodo_clase(cls,cadena):
        print('{0} {1}'.format("Cadena a mostrar:",cadena))

# La ventaja de usar metodos de clase es que no necesitan una instancia u
# objeto para ejecutar el metodo, ya que estos pueden llamarse sin realizar
# una instancia, asi tambien si existiera alguna el metodo puede ejecutarse
MiClase.metodo_clase("mi_cadena")


class MiClaseDos:
    pass

    """
    Un metodo estatico no puede acceder a los atributos de la clase, por lo
    tanto no cuenta con self como parametro del mismo, son como su nombre lo
    dice metodos estaticos para realizar operaciones sin requerir elementos de
    la clase.
    """
    @staticmethod
    def metodo_clase_static(cadena):
        print ('Cadena a mostrar en metodo estatico: {0}'.format(cadena))

# Al igual que con los metodos de clase no se requiere de una instancia para
# ejecutar el metodo, aunque de existir no habria problema alguno 
MiClaseDos.metodo_clase_static("string a imprimir")
