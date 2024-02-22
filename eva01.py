"""
Programa: eva01.py
Alumno: André Gael Aguilar Suárez
Matricula: 1723110015
Fecha: 29/01/2024
"""

class profesores(): #Constructor de la clase profesores
    id = None       #Define el valor del atributo id
    nombre = None   #Define el valor del atributo nombre
    materia = []    #Define el valor del atributo materia


    def __init__(self, id, nombre):  #Define el método init
        self.id = id                 #Asigna el parámetro id al atributo id
        self.nombre = nombre         #Asigna el parámetro nombre al atributo nombre
        self.materia = []            #Asigna el parámetro nombre al atributo nombre
        print("ClaseProfesor")       #Imprime "Clase Profesor"


    def califica(self):              #Define el método califica
        print("El profesor {} califica evaluaciones de la materia {}".format(self.nombre, self.materia[0]))  #Imprime el mensaje utilizando los atributos nombre y materia


    def pasaAsistencia(self):        #Define el método pasaAsistencia (podría nombrarse pasa_asistencia)
        print(f"El profesor {self.nombre} pasa asistencia")   #Imprime el mensaje utilizando un fprint para el atributo nombre

profesor1 = profesores(111,"Profesor 1")   #Crea el objeto profesor1 en la clase profesores
profesor1.materia.append("Materia 1")      #Asigna un valor al atributo materia
profesor1.materia.append("Materia 2")      #Asigna un valor al atributo materia
profesor1.califica()                       #Llama al método califica
profesor1.pasaAsistencia()                 #Llama al método pasaAsistencia