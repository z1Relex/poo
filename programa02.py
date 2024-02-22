"""
        Nombre: André Gael Aguilar Suarez
        Matrícula: 1723110015
        Grupo: TI21
        Fecha: 18/01/24
        Descripción: Creación de instancia de una clase llamando al método init.
"""

class A:                               # Define una clase llamada A
    matricula = None                     # Declara el atributo matrícula
    nombre = None                        # Declara el atributo nombre
    def __init__(self, matricula, nombre): # Define el método init
        print("Constructor de la clase A")   # Imprime "Constructor de la clase A"

objectA = A(111, "Gael")                            # Crea una instancia en la clase A
print(objectA.nombre)                  # Imprime el nombre (none)
