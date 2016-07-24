class Persona():

    def __init__(self,nombre,apellido_paterno,apellido_materno):
        """
        Inicializador, que se ejecuta inicialmente al crear un objeto de la clase
        con los atributos que lo requieran.
        Existe tambien un metodo llamado __new__ similar a este que es en realidad
        el constructor y asigna el espacio en memoria.
        Para generar una instancia o un objeto se requiere de 3 atributos.
        @nombre: Nombre de la persona
        @apellido_paterno: Apellido paterno de la persona
        @apellido_materno: Apellido materno de la persona
        """
        self.nombre = "Arturo"
        self.apellido_paterno = "Herrera"
        self.apellido_materno = "Trinidad"
        print("Objeto generado correctamente")

    def get_nombre(self):
        """
        Metodos de instancia propio de la clase
        @return: Atributo nombre
        """
        return '{0}'.format(self.nombre)

    def get_apellido_paterno(self):
        """
        Metodos de instancia propio de la clase
        @return: Atributo apellido_paterno
        """
        return '{0}'.format(self.apellido_paterno)

# Para la generacion de un objeto o instancia es necesario pasar los atributos que se requieren.
per = Persona("Juan Arturo", "Herrera", "Trinidad")

# Al ejecutar el metodo type podremos saber a que clase pertenece el objeto
print(type(per))
