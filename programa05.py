"""
    Nombre: André Gael Aguilar Suarez
    Matrícula: 1723110015
    Grupo: TI21
    Fecha: 18/01/24
    Descripción: Programa que crea una clase y un objeto e imprime 2 de sus métodos.
"""

class Alumno:                                      # Cream la clase Alumno
    matricula: None                                # Declara el atributo matricula
    nombre: None                                   # Declara el atributo nombre
    def __init__(self, matricula, nombre):         # Define el método init
        self.matricula = matricula                 # Asigna el valor del parámetro matricula al atributo matricula
        self.nombre = nombre                       # Asigna el valor del parámetro nombre al atributo nombre
        print("Objeto Alumno.")                    # Imprime Objeto Alumno
    def estudiar(self):                            # Define el método estudiar
        print(f"{self.nombre} estudia.")           # Imprime un mensaje
    def sumar(self, numero1, numero2):             # Define el método sumar
        suma = numero1 + numero2                   # Asigna a la variable suma el valor de la suma de numero1 y nuerom2
        print(f"{numero1} + {numero2} = {suma}.")  # Imprime la suma de ambos números
dejah = Alumno("1111", "Dejah")                    # Crea un objeto de la clase Alumno
dejah.estudiar()                                   # Llama al método estudiar del objeto dejah
dejah.sumar(5, 10)                                 # Llama al método sumar del objeto dejah
