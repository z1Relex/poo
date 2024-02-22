"""
        Nombre: André Gael Aguilar Suarez
        Matrícula: 1723110015
        Grupo: TI21
        Fecha: 18/01/24
        Descripción: Creación de instancia de una clase llamando al método init, asignando valores a los atributos
        y reasignación de valores de la instancia.
"""

class Alumnos:                                           # Define la clase Alumnos
    matricula: None                                      # Declara el atributo matricula
    nombre: None                                         # Declara el atributo nombre
    def __init__(self, matricula, nombre):               # Define el método init
            self.matricula = matricula                   # Asigna un valor a matricula
            self.nombre = nombre                         # Asigna un valor a nombre
            print("Objeto Alumnos")                      # Imprime "Objeto Alumnos"
objectAlumnos = Alumnos(111, "Juan")                     # Crea una instancia en la clase Alumnos
print(objectAlumnos.nombre)                              # Imprime "Objeto Alumnos" y el nombre
print(objectAlumnos.matricula )                          # Imprime "Objeto Alumnos" y la matrícula
objectAlumnos = Alumnos(nombre="John", matricula=222)    # Reasigna valores de la instancia
print(objectAlumnos.nombre)                              # Imprime "Objeto Alumnos" y el nombre 
print(objectAlumnos.matricula)                           # Imprime "Objeto Alumnos" y la matrícula
