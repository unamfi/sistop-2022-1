from threading import Semaphore, Thread, current_thread
from time import sleep
import random

#Semáforos que se implementan como indicadores para saber el orden de los micros 
YaBajaron = Semaphore( 0 )
YaSubieron = Semaphore ( 0 )
mutex = Semaphore( 1 )

#Clase que permite tener un checador en cada una de las paradas de la ruta.
class Checador:
    tiempo = 0
    tiempoPorPersona = 0.02

    #Método que indica cuanto tiempo se debe de esperar la micro para permitir que las personas suban
    def tiempoSubida( self, personasSuben, bus ): 
        self.tiempo = personasSuben*self.tiempoPorPersona
        print( "Micro:%d Suben: %d personas"%( bus, personasSuben ) )
        sleep( self.tiempo )
        YaSubieron.release()
        
    #Este método indica cuanto tiempo se debe esperar la micro para que la personas se bajen
    def tiempoBajada( self, personasBajan, bus ):
        self.tiempo = personasBajan*self.tiempoPorPersona
        print( "Micro:%d Bajan: %d personas"%( bus, personasBajan ) )
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
    print( "La micro:%d" %current_thread().nombre,"entra a la base" )

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
    print( "La micro:%d" %current_thread().nombre,"sale de la base y lleva: %d personas"%current_thread().personas )
    ruta()

#Método que simula las paradas que hay entre cada base, por las cuales tienen que pasar las micros
def ruta():
    global personasEnParadas, Ruta
    sleep( random.random() )

    #Itera por cada una de las paradas que tiene nuestro arreglo
    for it in range ( current_thread().paradas ):
        current_thread().parada += 1
        print( "La micro:%d" %current_thread().nombre,"entra a la parada:%d" %( current_thread().parada+1 ) )
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

    print( "La micro:%d" %current_thread().nombre,"sale de la parada: %d" %( current_thread().parada+1 ) )

print("=============================")
print("¡Hola! \nBuen día querido usuario, por favor digite el número de camiones que quiere simular:")
microbuses = int(input())

print("Ahora, digite el número de paradas que desea tener en su ruta:")
paradas = int(input())
print("=============================")

Ruta = []
personasEnParadas = []

if paradas>1:
    if microbuses<1:
        print("Sin microbuses no hay como subir pasajeros")
    else:
        for i in range(paradas):
            Ruta.append(Parada())
            personasEnParadas.append(0)

        for i in range (microbuses):
            Bus(i+1,paradas-1).start()
else:
    print("Se necesitan más de una parada para poder establecer una ruta")