'''
Programa: eva02.py
Nombre completo: André Gael Aguilar Suárez
Matricula: 1723110015
Fecha: 29/01/24
'''
class Libro:                   #Constructor de la clase Libro
    titulo = None              #Define el atributo titulo
    autor = None               #Define el atributo autor
    prestado = None            #Define el atributo prestado
    anio_publicacion = None    #Define el atributo anio_publicacion
    genero = None              #Define el atributo genero


    def __init__(self, titulo, autor, anio_publicacion, genero, prestado): #Define el método init
        self.titulo = titulo                                               #Asigna el parámetro titulo al atributo titulo
        self.autor = autor                                                 #Asigna el parámetro autor al atributo autor
        self.anio_publicacion = anio_publicacion                           #Asigna el parámetro anio_publicacion al atributo anio_publicacion
        self.genero = genero                                               #Asigna el parámetro genero al atributo genero
        self.prestado = prestado                                           #Asigna el parámetro prestado al atributo prestado
    
    def prestar(self):         #Define el método prestar
        self.prestado = True   #Establece el valor de prestado como verdadero

    def devolver(self):        #Define el método devolver
        self.prestado = False  #Establece el valor de prestado como falso
        
    def mostrar_informacion(self):                                         #Define el método mostrar_informacion
        print(f"Título: {self.titulo}\n")                                  #Imprime el valor del atributo título con fprint
        print(f"Autor: {self.autor}")                                      #Imprime el valor del atributo autor con fprint
        print(f"Año de publicación: {self.anio_publicacion}")              #Imprime el valor del atributo anio_publicacion con fprint
        print(f"Género: {self.genero}")                                    #Imprime el valor del atributo genero con fprint
        print(f"Prestado: {'Sí' if self.prestado else 'No'}\n")              #Imprime Sí o No dependiendo del valor del atributo prestado


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "Ficción",True)       #Crea el objeto libro1 en la clase Libro
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Ficción",True)  #Crea el objeto libro2 en la clase Libro
libro1.prestar()              #Llama al método prestar para libro1
libro1.mostrar_informacion()  #Llama al método mostrar_informacion para libro 1
libro2.mostrar_informacion()  #Llama al método mostrar_informacion para libro 2
libro1.devolver()             #Llama al método devolver para libro1
libro1.mostrar_informacion()  #Llama al método mostrar_informacion para libro 1
libro2.mostrar_informacion()  #Llama al método mostrar_informacion para libro 2


