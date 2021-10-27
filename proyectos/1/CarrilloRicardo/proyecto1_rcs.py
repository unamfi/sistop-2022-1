"""
ALUMNO: RICARDO CARRILLO SANCHEZ
MATERIA: SISTEMAS OPERATIVOS

"""
import os
import threading
import time 
import random
from lorem_text import lorem
import numpy as np

class Pregunta(threading.Thread): 

    """Clase: Pregunta

        esta clase represnta a un individuo pregunta, la cual tiene la tarea
        de encontrar coincidencias de la pregunta en un texto determinado

        :parametros
        id -> id del hilo a ejecutar
        pregunta -> pregunta que le corresponde buscar en el texto
        respuestas -> almacen temporal de las coincidencias encontradas con el texto
        intentosBusqueda -> cantidad de veces que se buscaron coincidencias en el texto y fueron positivas, es decir,
                            se encontro algo
    """ 
    def __init__(self, pregunta, id):
        super().__init__(target = self.anexar_respuestas, name=id)
        self.__id = id
        self.__pregunta = pregunta
        self.respuestas = []
        self.__intentosBusqueda = 0

    def encontre_algo(self):
        """Metodo encontre_algo

            este metodo devuelve un True en caso de que los intentos de busqueda sean afirmativos, es decir mayor a 0.

        """
    
        return True if self.__intentosBusqueda > 0 else False  

    def buscar_coincidencias(self):

        """Metodo: buscar_coincidencias

            este metodo se encarga de la 'simulacion' de busqueda dentro de un documento de texto, cada hilo se puede demorar 
            en la tarea hasta 1 segundo, y existe una probabilidad de exito de encontrar una respuesta de 0.65 , en caso de 
            encontrar coincidencias, el hilo incrementa el atributo, intentosBusqueda. Ademas de imprimir al usuario el 
            estado de la busqueda, es decir:

            * buscando
            * encontre n coincidencias

            Por ultimo el metodo almacenara las coincidencias en su atributo correspondiente y en la variable global respuestas_listas
        """
        global respuestas_listas
        
        time.sleep(random.randint(0,1))
        print(f'{ft["reset"]}Soy {ft["cyan"]}{ft["bold"]}({self.__id}) -> {ft["amarillo"]}{ft["bold"]}buscando...{ft["reset"]}')
       
        while np.random.choice(2, 1, p=[0.35,0.65]): #regresa 0 o 1, tomando en cuenta una probabilidad determinada
            self.respuestas.append(lorem.paragraph()) #texto aleatorio registrado como respuesta
            self.__intentosBusqueda += 1
            print(f'Soy {ft["cyan"]}{ft["bold"]}({self.__id}) {ft["verde"]}-> encontre {ft["bold"]}{len(self.respuestas)} {ft["disable"]}coincidencias{ft["reset"]}')

        
    def anexar_respuestas(self): 

        """Metodo: anexar_respuestas

            Este metodo se encarga de anexar las respuestas del algoritmo previo al archivo txt correspondiente. EL algoritmo del codigo es el siguiente

            buscar()
            si encontre coincidencias: 
                disminuir preguntas restantes
                anadir coincidencias a txt
            
            de otra forma
                disminuir preguntas restantes

            Hay que tomar en cuenta que sobre este metodo se realiza la ejecucion de instrucciones del hilo, por lo que es importante tomar en cuenta que este metodo 
            esta regido bajo un permiso del controlador, es decir, el controlador sera el encargado de dar la autorizacion al hilo de almacenar sus archivos en el txt

        """
        global mutex_resultados, barrera_archivo, \
            respuestas_listas, pregunta_actual, senal_listo, \
            preguntas_pendientes, exitos, no_encontrados
        
        self.buscar_coincidencias()

        if self.encontre_algo():  
            
            mutex_resultados.acquire()
            respuestas_listas = self.respuestas
            pregunta_actual = self.__id
            preguntas_pendientes -= 1 
            exitos.append(self.__id)
            
            barrera_archivo.release()
            print(f'Soy {ft["cyan"]}{ft["bold"]}({self.__id}) {ft["violeta"]}-> {ft["bold"]}agregare algo a respuestas.txt{ft["reset"]}')
            archivo_respuestas = open('archivo_respuestas.txt', 'a')

            if len(respuestas_listas) > 0:

                archivo_respuestas.write(f'\nResultados para pregunta {pregunta_actual}'+os.linesep)
                for r in respuestas_listas:
                    archivo_respuestas.write(f'\n\tResultado {self.__id} - '+ r + os.linesep)
                archivo_respuestas.close()    

            mutex_resultados.release()

        else: # en caso de que no se encuentren resultados, unicamente se 
            print(f'{ft["reset"]}Soy {ft["cyan"]}{ft["bold"]}({self.__id}) -> {ft["rojo"]}{ft["bold"]}no encontre coincidencias para la pregunta {self.__id}')    
            mutex_resultados.acquire()  
            
            pregunta_actual = self.__id
            preguntas_pendientes -= 1 
            no_encontrados.append(self.__id)
            mutex_resultados.release()

        senal_listo.release()
   


class Controlador(threading.Thread): 

    """Clase: Controlador

        Esta clase se encarga de la administracion de las preguntas

        :parametros
        id (int) : id del hilo a ejecutar    
    """
    def __init__(self, id):
        super().__init__(target = self.checar, name=id)
        self.__id = id

    def resumen(self):
        """Metodo: resumen

           Se encarga de imprimir un resumen en terminal de las preguntas encontradas
           y las no encontradas 
        """
        global exitos, no_encontrados

        print(f'{ft["fazu"]}Preguntas encontradas: {exitos}{ft["reset"]}')
        print(f'{ft["fmag"]}Preguntas no encontradas: {no_encontrados}{ft["reset"]}')

    def checar(self):
        """Metodo: checar

            Funcion que se ejecutara al comenzar la clase, este metodo se encarga de la 
            autorizacion por parte de las preguntas para anadir sus resultados dentro del
            archivo de texto. 

        """
        global barrera_archivo, \
               archivo_respuestas, senal_listo, pregunta_actual, \
               preguntas_pendientes, exitos, no_encontrados

        while preguntas_pendientes:     
            senal_listo.acquire()

            if pregunta_actual in exitos:
                barrera_archivo.release()
            
            print(f'{ft["fab"]}{ft["bb"]}CONTROLADOR -> tengo {preguntas_pendientes} preguntas pendientes{ft["reset"]}')

        self.resumen()

        
ft = {  'reset' : '\033[0m',  #diccionario de interrupciones para salida de color en terminal
        'bold' : '\033[1m',
        'disable' : '\033[2m',
        'amarillo': '\033[;33m',
		'violeta': '\033[;35m',
	    'verde': '\033[;32m',
	    'rojo': '\033[;31m',
	    'blanco': '\033[;37m',
	    'cyan': '\033[;36m', 
        'naranja': '\033[;33m',
        'fmag' : '\033[;105m',
        'fazu' : '\033[;104m',
        'fab' : '\033[;107m',
        'bb': '\033[1;30m'}

os.system('clear')
os.system('cat /dev/null > archivo_respuestas.txt') #al comenzar a ejecutar el programa borra el contenido previo del archivo

with open('preguntas.txt','r') as f:
    tarea = f.readlines()

#mutex para la proteccion de escritura y lectura de cada hilo al archivo de resultados
mutex_resultados = threading.Semaphore(1) 

#barrera que evitara el acceso mutuo al archivo 
barrera_archivo = threading.Semaphore(0)

#senal para indicar al controlador que la pegunta termino su busqueda
senal_listo = threading.Semaphore(0)

#auxiliar de la pregunta actual
pregunta_actual = 0

#lista auxiliar para almacenar las preguntas a las que se les encontro una respuesta
exitos = []

#lista auxiliar para almacenar las preguntas a las que no se les encontro una respuesta
no_encontrados = []

#auxiliar de la cantidad de preguntas pendientes, se inicializa con la longitud de 
#lista en la que se almacenan las preguntas
preguntas_pendientes = len(tarea)


Controlador(1).start()

for i in tarea: i = i.strip()

for m in range(len(tarea)):
    Pregunta(tarea[m],m+1).start()

# os.system('nano archivo_respuestas.txt')