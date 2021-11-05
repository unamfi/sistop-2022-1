import random
from queue import Queue
import time
import copy

# Tiempo de respuesta, tiempo total 
# Tiempo de espera E = T - t
# Proporcion de penalizacion P = T/t

class Proceso:
    def __init__(self, id, llegada, ticks) -> None:
        self.id = id
        self.llegada = llegada
        self.ticks = ticks

def FCFS(procesos:Proceso):
    cola_procesos = Queue(len(procesos))

    proceso_actual = Proceso("n", 0, 0)
    ticks_transcurridos = 0
    
    inicio = 0
    T = 0
    E = 0
    P = 0

    t = []
    e = []
    p = []

    orden = ""

    while cola_procesos.empty() == False or (len(procesos) != 0) or (proceso_actual.ticks != 0):
        
        for i in range(len(procesos)): 
            if ticks_transcurridos == procesos[i].llegada:
                cola_procesos.put(procesos[i])

                espera = inicio - procesos[i].llegada
                t.append( procesos[i].ticks + espera )
                e.append( espera )
                p.append( (procesos[i].ticks + espera) / procesos[i].ticks )
                inicio += procesos[i].ticks

                procesos[i] = None
        
        procesos = list(filter(lambda p: p != None, procesos))

        if proceso_actual.ticks == 0:
            if cola_procesos.empty() == False:
                proceso_actual = cola_procesos.get()
            else:
                proceso_actual = Proceso("n", 0, 0)
        
        if proceso_actual.ticks > 0:
            proceso_actual.ticks -= 1

        orden += proceso_actual.id
        #print(proceso_actual.id, end="")
        ticks_transcurridos += 1       

    for i in range( len( t ) ): 
        T += t[ i ]
    T = T / len(t)

    for i in range( len( e ) ): 
        E += e[ i ]
    E = E / len(e)

    for i in range( len( p ) ):  
        P += p[ i ]
    P = P / len(p)

    print("\n\nFCFS: T=%.2f, E=%.2f, P=%.2f" %( T, E, P ))
    print(orden)


def Ronda(procesos):
    lista_procesos = []
    procesos_despachados = 0
    num_procesos = len(procesos)

    q = 1
    ticks_transcurridos = 0
    index = 0

    inicio = 0

    T = 0
    E = 0
    P = 0

    t = []
    e = []
    p = []

    orden = ""

    tiempos_requeridos = {}

    while procesos_despachados < num_procesos:

        if index >= len(lista_procesos):
            index = 0

        if len(lista_procesos) > 0: 
            lista_procesos[index].ticks -= 1
            orden += lista_procesos[index].id
            #print(lista_procesos[index].id, end="")
        
            index += 1
        # porque si hay tiempos muertos queremos que se represente
        else: 
            orden += "n"

        for i in range(len(lista_procesos)):
            if lista_procesos[i].ticks == 0:
                procesos_despachados += 1
                t.insert(0, ticks_transcurridos - lista_procesos[i].llegada)
                e.append(t[0] - tiempos_requeridos[lista_procesos[i].id])
                p.append(t[0] / tiempos_requeridos[lista_procesos[i].id])
                inicio += tiempos_requeridos[lista_procesos[i].id]
                lista_procesos[i] = None 
                if index > 0:
                    index -= 1

        lista_procesos = list(filter(lambda p: p != None, lista_procesos))

        for i in range(len(procesos)): 
            if ticks_transcurridos == procesos[i].llegada:
                lista_procesos.append(procesos[i])
                tiempos_requeridos[procesos[i].id] = procesos[i].ticks
                procesos[i] = None
        procesos = list(filter(lambda p: p != None, procesos))

        ticks_transcurridos += 1

    for i in range( len( t ) ): 
        T += t[ i ]
    T = T / len(t)

    for i in range( len( e ) ): 
        E += e[ i ]
    E = E / len(e)

    for i in range( len( p ) ):  
        P += p[ i ]
    P = P / len(p)

    print("\nRR1: T=%.2f, E=%.2f, P=%.2f" %( T, E, P ))
    print(orden)

def Ronda4(procesos):
    lista_procesos = []
    procesos_despachados = 0
    num_procesos = len(procesos)

    q = 0
    ticks_transcurridos = 0
    index = 0

    inicio = 0

    T = 0
    E = 0
    P = 0

    t = []
    e = []
    p = []

    orden = ""

    tiempos_requeridos = {}

    while procesos_despachados < num_procesos:

        if index >= len(lista_procesos):
            index = 0

        if len(lista_procesos) > 0: 
            lista_procesos[index].ticks -= 1
            orden += lista_procesos[index].id
            #print(lista_procesos[index].id, end="")

            q += 1

            if q == 4:
                index += 1
                q = 0
        # porque si hay tiempos muertos queremos que se represente
        else: 
            orden += "n"

        for i in range(len(lista_procesos)):
            if lista_procesos[i].ticks == 0:
                procesos_despachados += 1
                #print(f"saliendo{lista_procesos[i].id}, ticks trans {ticks_transcurridos}")
                t.insert(0, ticks_transcurridos - lista_procesos[i].llegada)
                e.append(t[0] - tiempos_requeridos[lista_procesos[i].id])
                p.append(t[0] / tiempos_requeridos[lista_procesos[i].id])
                inicio += tiempos_requeridos[lista_procesos[i].id]
                lista_procesos[i] = None 

                if index > 0:
                    index -= 1
                q = 0
        
        lista_procesos = list(filter(lambda p: p != None, lista_procesos))

        for i in range(len(procesos)): 
            if ticks_transcurridos == procesos[i].llegada:
                lista_procesos.append(procesos[i])
                tiempos_requeridos[procesos[i].id] = procesos[i].ticks
                procesos[i] = None
        procesos = list(filter(lambda p: p != None, procesos))

        ticks_transcurridos += 1

    for i in range( len( t ) ): 
        T += t[ i ]
    T = T / len(t)

    for i in range( len( e ) ): 
        E += e[ i ]
    E = E / len(e)

    for i in range( len( p ) ):  
        P += p[ i ]
    P = P / len(p)

    print("\nRR4: T=%.2f, E=%.2f, P=%.2f" %( T, E, P ))
    print(orden)

def copiar_lista_objetos(lista):
    aux = []
    for p in lista:
        aux.append(copy.deepcopy(p))
    return aux


ASCII_A = 65
NUM_PROCESOS = 5

def main():

    # inicializa los procesos
    num_rondas = int(input("Ingrese el numero de rondas que quiere ejecutar: "))

    num_ronda = 0
    print(f"\nRonda {num_ronda}, tabla diapositivas:")

    procesos = []

    lista_ejemplo_profe = ["A", 0, 3 ], ["B", 1, 5 ], ["C", 3, 2 ], ["D", 9, 5 ], ["E", 12, 5 ]

    for elm in lista_ejemplo_profe:
        procesos.append(Proceso(elm[0], elm[1], elm[2]))

    for p in procesos:
        print(f" {p.id}:{p.llegada} t: {p.ticks}", end=";")

    FCFS(copiar_lista_objetos(procesos))
    Ronda(copiar_lista_objetos(procesos))
    Ronda4(copiar_lista_objetos(procesos))
    
    num_ronda += 1

    while num_ronda <= num_rondas:  

        print(f"\nRonda {num_ronda}:")
        procesos = []

        for i in range(NUM_PROCESOS):
            procesos.append(Proceso(chr(ASCII_A + i), random.randint(0, 10), random.randint(1, 10)))
        
        for p in procesos:
            print(f" {p.id}:{p.llegada} t: {p.ticks}", end=";")

        FCFS(copiar_lista_objetos(procesos))
        Ronda(copiar_lista_objetos(procesos))
        Ronda4(copiar_lista_objetos(procesos))

        num_ronda += 1


if __name__ == "__main__":
    main()