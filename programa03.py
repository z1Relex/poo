"""
        Nombre: André Gael Aguilar Suarez
        Matrícula: 1723110015
        Grupo: TI21
        Fecha: 18/01/24
        Descripción: Creación de instancia de una clase llamando al método init, asignando valores a los atributos.
"""

class Alumnos:                              # Define la clase Alumnos
    matricula = None                        # Declara el atributo matrícula
    nombre = None                           # Declara el atributo nombre
    def __init__(self, matricula, nombre):  # Define el metodo init
        self.matricula = matricula          # Asigna un valor a matrícula
        self.nombre = nombre                # Asigna un valor a nombre
        print("Objeto Alumnos")             # Imprime "Objeto Alumnos"
objectA = Alumnos(111, "Gael")              # Crea una instancia en la clase Alumnos
print(objectA.nombre)                       # Imprime el nombre
