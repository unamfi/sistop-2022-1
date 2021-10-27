#Integrantes:
#Díaz Hernández Marcos Bryan.
#Fuerte Martínez Nestor Enrique.

from tkinter import *
from PIL import ImageTk, Image
from threading import Semaphore, Thread, current_thread
from time import sleep
import random

#Se crea el la venta principal de ejecución del gráfico.
ventana = Tk()

#Se declaran las variables para poder obtener los valores de los cuadros de entrada
paradasSTR = StringVar()
microbusesSTR = StringVar()

Ruta = []
personasEnParadas = []

#Semáforos que se implementan como indicadores para saber el orden de los micros 
YaBajaron = Semaphore( 0 )
YaSubieron = Semaphore ( 0 )
mutex = Semaphore( 1 )

#Definición de atributos de la ventana
ventana.title("RUTA DE MICROS")
ventana.resizable(False, False)
ventana.geometry("900x400")

#Se inserta una imagen como fondo
microbus = ImageTk.PhotoImage(Image.open('A.jpg'))
lblMicrobus = Label(ventana, image = microbus).place(x = 0, y = 0)

#Se crea un recuadro donde se colocan las instrucciones para el usuario
FrameE = Frame()
FrameE.config(bg = "SteelBlue1")
FrameE.config(width = "350", height = "150")
FrameE.pack(side = "left",anchor = "nw")

#Se crea un recuadro donde se colocan las impresiones que se habían hecho en la versión secuencial
FrameS=Frame()
FrameS.config(bg = "orange")
FrameS.config(width = "350", height = "250")
FrameS.pack(side = "right", anchor = "e")

#Se coloca el texto correspondiente para darle las intrucciones al usuario.
Label(FrameE, text = "Por favor, ingrese los valores que se indican:", bg = "yellow3", font = ("Arial",13) ).place(x = 0, y = 0)
Label(FrameE, text = "Cantidad de Paradas: ", bg = "yellow3", font=("Arial Bold",10)).place(x = 0, y = 35)
Label(FrameE, text = "Cantidad de Microbuses: ", bg = "yellow3", font=("Arial Bold",10)).place(x = 0, y = 65)

#Se colocan los recuadros para que se puedan insertar valores
Entry(FrameE, textvariable = paradasSTR).place(x = 145, y = 35)
Entry(FrameE, textvariable = microbusesSTR).place(x = 165, y = 65)

#Se crea el botón correspondiente para enviar los valores a la funcion de inicio
Button(FrameE, text = "Envio",width = 7,command=lambda:iniciar()).place(x=100,y=100)

#Se configura el recuadro de la salida de las impresiones y 
Label(FrameS, text = "Movimientos en la ruta", bg="SteelBlue1", font = ("Arial",13)).grid(row = 0, column = 0)
action = Text(FrameS, width = 50, height = 20)
action.grid(row = 1, column = 0, padx = 10, pady = 10)

#Se crea el barra scroll para poder visualizar las impresiones de toda la implementación
scrollVert = Scrollbar(FrameS, command = action.yview)
scrollVert.grid(row = 1,column = 1, sticky = "nsew")
action.config(yscrollcommand = scrollVert.set)


def iniciar():
    global paradas, microbuses
    action.delete('1.0',END) #Limpia las impresiones del recuadro
    
    try:
        paradas = int(paradasSTR.get())
        microbuses = int(microbusesSTR.get())
    except ValueError:
        action.insert(INSERT,"Entrada erronea\n")
    
    if paradas>1:
        if microbuses<1:
            action.insert(INSERT,"Sin microbuses no hay como subir pasajeros\n")
        else:
            for i in range(paradas):
                Ruta.append(Parada())
                personasEnParadas.append(0)

            for i in range (microbuses):
                Bus(i+1,paradas-1).start()

    else:
        action.insert(INSERT,"Se necesitan más de una parada para poder establecer una ruta\n") 

#Clase que permite tener un checador en cada una de las paradas de la ruta.
class Checador:
    tiempo = 0
    tiempoPorPersona = 0.02

    #Método que indica cuanto tiempo se debe de esperar la micro para permitir que las personas suban
    def tiempoSubida( self, personasSuben, bus ): 
        self.tiempo = personasSuben*self.tiempoPorPersona
        action.insert(INSERT,"Micro 🚐:{} Suben:{} personas\n".format(bus, personasSuben))
        sleep( self.tiempo )
        YaSubieron.release()

    #Este método indica cuanto tiempo se debe esperar la micro para que la personas se bajen
    def tiempoBajada( self, personasBajan, bus ):
        self.tiempo = personasBajan*self.tiempoPorPersona
        action.insert(INSERT,"Micro 🚐:{} Bajan:{} personas \n".format(bus, personasBajan))
        sleep( self.tiempo )
        YaBajaron.release()

#Esta clase permite tener paradas con objetos de tipo checador para ir organizando las micros
class Parada:
    checador = Checador()
    parada = Semaphore( 1 )

#Clase que crea los hilos de tipo microbus
class Bus( Thread ):
    capacidad = 50
    paradas = 0

    def __init__( self, Nombre, Paradas ):
        super().__init__( target = base, args = []  )
        self.personas = 0
        self.parada = 0
        self.nombre = Nombre
        self.paradas = Paradas

#Se calcula aleatoriamente un numero de personas que quieran subir a la micro en las paradas intermedias entre bases
def paradaSube( parada, capacidad ) -> int :
    global personasEnParadas
    personasEnParadas[ parada ]  = random.randint( 0, capacidad-42 )
    return personasEnParadas[ parada ]

#Método que crea un numero aleatorio de personas que quieran bajar
def paradaBaja( personas ) -> int:
    return random.randint( 0, personas )

#Método que crea un numero aletaorio de personas que quieran subir estando en la base( son más porque en las bases de las micros hay más gente que en las otras paradas)
def filaBase( capacidad, parada ) -> int:
    global personasEnParadas
    personasEnParadas[ parada ] += random.randint( 0, capacidad-35 )
    return personasEnParadas[ parada ]

#Método encargado de simular la base donde empiezan todas las micros
def base():
    global personasEnParadas, Ruta

    #Mutex para que entren a la base en orden
    mutex.acquire()
    #Mutex para que solo una micro pueda estar subiendo gente
    Ruta[ current_thread().parada ].parada.acquire()
    action.insert(INSERT,"La micro 🚐:{} entra a la base\n".format(current_thread().nombre))

    #Comienza a subir gente hasta que se llene o pase el tiempo
    for tiempoEnBase in range(5):  #El micro empieza en la base 
        if ( tiempoEnBase < 5 and current_thread().personas < current_thread().capacidad ):  #Si llega a 5 minutos o se llena el bus se va a la primer parada
            if( filaBase( current_thread().capacidad, current_thread().parada ) <= current_thread().capacidad - current_thread().personas ): #Checa si puede meter a todos los que estan en la fila
                current_thread().personas += personasEnParadas[ current_thread().parada ]
                Ruta[ current_thread().parada ].checador.tiempoSubida( personasEnParadas[ current_thread().parada ], current_thread().nombre )
                personasEnParadas[ current_thread().parada ] -= personasEnParadas[ current_thread().parada ]
                YaSubieron.acquire()
            else:   #Si no puede meter a todos, solo sube la cantidad de lugares que tiene disponibles 
                personasSinLugar = personasEnParadas[ current_thread().parada ] - ( current_thread().capacidad - current_thread().personas ) #Auxiliar guarda la cantidad de personas que no van a subir
                current_thread().personas += personasEnParadas[ current_thread().parada ] - personasSinLugar  #Subo al bus la cantidad de personas que pueden entrar
                Ruta[current_thread().parada].checador.tiempoSubida( personasEnParadas[ current_thread().parada ] - personasSinLugar, current_thread().nombre )
                personasEnParadas[ current_thread().parada ] = personasSinLugar  #Se restan  las personas que si obtuvieron lugar
                personasSinLugar  = 0
                YaSubieron.acquire()
        else:
            continue

    #Libera la base y puede otro hilo empezar a subir gente
    Ruta[ current_thread().parada ].parada.release()
    mutex.release()
    action.insert(INSERT,"La micro 🚐:{} sale de la base y lleva:{} personas\n".format(current_thread().nombre,current_thread().personas))
    ruta()

#Método que simula las paradas que hay entre cada base, por las cuales tienen que pasar las micros
def ruta():
    global personasEnParadas, Ruta
    sleep( random.random() )

    #Itera por cada una de las paradas que tiene nuestro arreglo
    for it in range ( current_thread().paradas ):
        current_thread().parada += 1
        action.insert(INSERT,"La micro 🚐:{} entra a la parada:{}\n".format(current_thread().nombre,current_thread().parada+1))
        Ruta[ current_thread().parada ].parada.acquire()

        #Verifica que haya personas que puedan bajar, y se saca un numero aleatorio para la cantidad que bajan
        if( current_thread().personas > 0 ):
            personasQueBajaron = paradaBaja( current_thread().personas )
            current_thread().personas -=  personasQueBajaron
            Ruta[ current_thread().parada ].checador.tiempoBajada( personasQueBajaron, current_thread().nombre )
            YaBajaron.acquire()

        #Si hay personas esperando el bus, calculamos cuantos podemos subir
        if ( paradaSube( current_thread().parada, current_thread().capacidad ) >= 0 ):
            if( current_thread().capacidad - current_thread().personas >= personasEnParadas[ current_thread().parada ] ):
                current_thread().personas += personasEnParadas[ current_thread().parada ]   
                Ruta[ current_thread().parada ].checador.tiempoSubida( personasEnParadas[ current_thread().parada ], current_thread().nombre ) #El checador se fija que bajen las personas y que pase el tiempo adecuado para cada persona               
                personasEnParadas[ current_thread().parada ] -= personasEnParadas[ current_thread().parada ]
                YaSubieron.acquire()

            if ( current_thread().personas < current_thread().capacidad and current_thread().capacidad - current_thread().personas < personasEnParadas[ current_thread().parada ] ):
                personasSinLugar = personasEnParadas[ current_thread().parada ] - ( current_thread().capacidad - current_thread().personas ) #Auxiliar guarda la cantidad de personas que no van a subir
                current_thread().personas += personasEnParadas[ current_thread().parada ] - personasSinLugar  #Subo al bus la cantidad de personas que pueden entrar
                Ruta[ current_thread().parada].checador.tiempoSubida(personasEnParadas[ current_thread().parada ] - personasSinLugar, current_thread().nombre ) #El checador se fija que suban las personas y que pase el tiempo adecuado para cada persona               
                personasEnParadas[ current_thread().parada ] = personasSinLugar  #Se restan  las personas que si obtuvieron lugar
                YaSubieron.acquire()

        sleep( random.random() )
        Ruta[ current_thread().parada ].parada.release()

    action.insert(INSERT,"La micro 🚐:{} sale de la parada:{}\n".format(current_thread().nombre,current_thread().parada+1,))


ventana.mainloop()