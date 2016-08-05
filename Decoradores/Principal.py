"""
Un decorador es una funcion que recibe como parametro otra funcion y realizar
cualquier operacion que se le indique al decorador.
"""
def MiDecorador(f):
    print("Este es el nombre de la funcion {}".format(f.__name__))

"""
Anteponiendo el signo arroba se puede decorar a una funcion
"""
@MiDecorador
def AbrirPuerta():
    print ("Abrir la puerta")

@MiDecorador
def CerrarPuerta():
    print ("Cerrar la puerta")

"""
Para decorar las funciones AbrirPuerta y CerrarPuerta se realiza de la siguiente
forma. En este ejemplo no olvidar remover los decoradores de las funciones
anteriores
"""
#MiDecorador(AbrirPuerta)
#MiDecorador(CerrarPuerta)


### Usando clases como decoradores
print("OTRO EJEMPLO DE DECORADORES")


class ClaseDecorador():
    """
    Clase decoradora
    """
    def __init__(self,fn):
        self.fn = fn

    def __call__(self,n1,n2):
        print(n1+n2)

@ClaseDecorador
def function_a_decorar(n1,n2):
    print ("La suma es {}".format(n1+n2))

print(function_a_decorar(2,4))
