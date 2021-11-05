"""
tarea 3
RICARDO CARRILLO SANCHEZ
"""


import random 

def promedio(lista) : return sum(lista)/len(procesos)

def tiempo_promedio_espera(T,procesos): #tomando en cuenta que la espera es T-t
    E = []

    q = 0
    for p in procesos: 
        E.append(T[q] - procesos[p][1])
        q += 1
    return promedio(E)

def promedio_penalizacion(T,procesos): #tomando en cuenta que la espera es T/t
    P = []
    q = 0
    
    for p in procesos: 
        P.append(T[q] / procesos[p][1])
        q += 1
    
    return promedio(P)


def FCFS(procesos): 
    respuesta_procesos = []
    T = [] 

    t = procesos['A'][1]
    for p in procesos:   #Obteniendo los tiempos de respuesta de todos los procesos 
        t = t + procesos[p][1] if p != 'A' else t 
        respuesta_procesos.append(t) 
        T.append(t-procesos[p][0])


    print(f'FCFS/FIFO: \nT = {promedio(T)} | E = {tiempo_promedio_espera(T,procesos)} | P = {promedio_penalizacion(T,procesos)}')

def encuentra_llave(procesos,val): 
    for key, value in procesos.items():
        if value==val:
            return key


def SPN(procesos): 
    valores_procesos = list(procesos.values())
    aux_vp = valores_procesos
    llaves_procesos = list(procesos.keys())

    orden_ejecucion = []
    respuesta_procesos = []
    T = []
    
    orden_ejecucion.append([llaves_procesos.pop(0), valores_procesos.pop(0)])    
    valores_procesos = sorted(valores_procesos, key=lambda x: x[1])
    
    for p in range(len(valores_procesos)):
        orden_ejecucion.append([encuentra_llave(procesos,valores_procesos[p]), valores_procesos[p]])
    
    for p in range(len(aux_vp) + 1):
        a = orden_ejecucion[p][1][1] if p == 0 else respuesta_procesos[p-1] + orden_ejecucion[p][1][1]
        respuesta_procesos.append(a)
        T.append(respuesta_procesos[p] - orden_ejecucion[p][1][0])

    
    print(f'SPN: T = {promedio(T)} | E = {tiempo_promedio_espera(T,procesos)} | P = {promedio_penalizacion(T,procesos)}')


"""
Generamos diccionario de procesos los cuales la clave del mismo 
representa el nombre del proceso, mientras que el contenido de la
clave sera una lista de dos elementos los cuales representaran el 
tiempo de llegada del proceso ademas de la duracion del proceso, es 
decir: 

proceso     llegada    duracion
   a     : [    #   ,     #     ]
"""

for intentos in range(0,5):
    #Diccionario de procesos inicializado
    procesos = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}

    llegada_proceso = 0

    for p in procesos:
        duracion = random.randint(1,5)
        procesos[p].append(llegada_proceso)  
        procesos[p].append(duracion)  #duracion del proceso
        llegada_proceso += random.randint(1, duracion)

    print(f'------------------------Corrida: {intentos}-------------------------\n')
    print (f'procesos {procesos} \n') 

    FCFS(procesos)
    SPN(procesos)

    print('---------------------------------------------------------------------\n')
