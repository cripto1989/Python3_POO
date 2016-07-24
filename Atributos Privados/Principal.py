class MiClase():
    """
    Para el manejo de atributos privados se necesita anteceder al atributo de
    dos guiones bajos '__'.
    """

    def __init__(self, atributo, atributo_privado):
        self.mi_atributo = atributo
        self.__mi_atributo_privado = atributo_privado
        print("Objeto creado correctamente")

    def get_mi_atributo_privado(self):
        return '{0}'.format(self.__mi_atributo_privado)

    def set_mi_atributo_privado(self,nuevo_valor):
        self.__mi_atributo_privado = nuevo_valor

obj = MiClase("valor", "valor privado")
# Para acceder al atributo privado se tiene que realizar un metodo de instancia
# que retorne el valor del mismo, este atributo por lo comun se usa para solo
# lectura
print(obj.get_mi_atributo_privado())
# Si se intenta acceder al valor del atributo privado desde la instancia se
# generara un error que indicara que la instancia no tiene el atributo
print(obj.__mi_atributo_privado)
# Para asignar un nuevo valor al atributo privado se define un nuevo metodo de
# instancia que se encargara de realizar la modificacion del mismo.
print(obj.set_mi_atributo_privado("nuevo valor"))
print(obj.get_mi_atributo_privado())
