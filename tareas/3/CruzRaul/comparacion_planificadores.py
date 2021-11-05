from random import randint
import copy
procesos_terminados = 5

def crear_cargas():
    tiempo_llegada = 0
    cargas = []
    cargas.append(['A',randint(1, 10),0])
    
    for i in range(66,70):
        # t es el tiempo requerido
        t = randint(1, 10)
        tiempo_llegada = tiempo_llegada + randint(1, 5)
        # Se crea una lista con los procesos generados de forma aleatoria
        cargas.append([chr(i),t,tiempo_llegada])
    
    print(cargas)
    return cargas

def fifo(cargas):
    inicio = 0
    fin = 0
    orden = ''
    T = 0
    T_total = 0
    E = 0
    E_total = 0
    P = 0
    P_total = 0
    total = 0
    for i in range(len(cargas)):
        # Se imprime el orden de ejecución de los procesos, al ser FIFO se ejecutan como fueron llegando
        orden = orden + (cargas[i][0]*cargas[i][1])
        #Comprobamos si es el primer elemento
        if cargas[i][2] == 0:
            inicio = 0
            fin = cargas[i][1]
            T = fin
            T_total += T
            E = 0
            E_total += E
            P = T/cargas[0][1]
            P_total += P
        #Si no es el primer elemento, se procede con normalidad
        else:
            inicio += cargas[i-1][1]
            fin = inicio + cargas[i][1]
            T = fin - cargas[i][2]
            T_total += T
            E = T - cargas[i][1]
            E_total += E
            P = T/cargas[i][1]
            P_total += P
        total += cargas[i][1]
    #Calculamos promedios
    T_total = T_total/len(cargas)
    E_total = E_total/len(cargas)
    P_total = P_total/len(cargas)
    print('   tot:',total)
    print('FCFS: T=%.2f, E=%.2f, P=%.2f' %(T_total,E_total,P_total))
    print(orden)
    
def rr1(cargas):
    #Se usa deepcopy() debido a que así clona todos los objetos de la lista
    cargasRR = copy.deepcopy(cargas)
    tick_actual = 0
    fin = 0
    T = 0
    T_total = 0
    E = 0
    E_total = 0
    P = 0
    P_total = 0
    orden = ''
    cola_terminados = []
    procesos_terminados = 5
    
    while procesos_terminados > 0:
        for i in range(len(cargasRR)):
            # Comprobamos que el tick actual sea igual a la hora de llegada
            # Comprobamos que el tiempo requerido no sea 0 porque el proceso haya terminado
            if(tick_actual>=cargasRR[i][2] and cargasRR[i][1] > 0):
                orden += cargasRR[i][0]
                cargasRR[i][1] -= 1
                tick_actual += 1
            if(cargasRR[i][1] == 0 and cargasRR[i][0] not in cola_terminados):
                fin = tick_actual
                T = fin - cargasRR[i][2]
                T_total += T
                E = T - cargas[i][1]
                E_total += E
                P = T/cargas[i][1]
                P_total += P
                cola_terminados.append(cargasRR[i][0])
                procesos_terminados -= 1
                
    T_total = T_total/len(cargasRR)
    E_total = E_total/len(cargasRR)
    P_total = P_total/len(cargasRR)
    print('RR1: T=%.2f, E=%.2f, P=%.2f' %(T_total,E_total,P_total))
    print(orden)
    

def rr4(cargas):
    #Se usa deepcopy() debido a que así clona todos los objetos de la lista
    cargasRR = copy.deepcopy(cargas)
    tick_actual = 0
    fin = 0
    T = 0
    T_total = 0
    E = 0
    E_total = 0
    P = 0
    P_total = 0
    orden = ''
    cola_terminados = []
    procesos_terminados = 5
    
    while procesos_terminados > 0:
        for i in range(len(cargasRR)):
            # Comprobamos que el tick actual sea igual a la hora de llegada
            # Comprobamos que el tiempo requerido no sea 0 porque el proceso haya terminado
            if(tick_actual>=cargasRR[i][2] and cargasRR[i][1] > 0):
                if cargasRR[i][1] >= 4:
                    tick_actual += 4
                    cargasRR[i][1] -= 4
                    orden += cargasRR[i][0]*4
                else:
                    orden += cargasRR[i][0]*cargasRR[i][1]
                    tick_actual += cargasRR[i][1]
                    cargasRR[i][1] -= cargasRR[i][1]
                    if(cargasRR[i][1] == 0 and cargasRR[i][0] not in cola_terminados):
                        #print(cargasRR)
                        fin = tick_actual
                        T = fin - cargasRR[i][2]
                        #print(T)
                        T_total += T
                        E = T - cargas[i][1]
                        #print(E)
                        E_total += E
                        P = T/cargas[i][1]
                        #print(P)
                        P_total += P
                        cola_terminados.append(cargasRR[i][0])
                        procesos_terminados -= 1
                    if cargasRR[i-1][1] <= 4:
                        orden += cargasRR[i-1][0]*cargasRR[i-1][1]
                        tick_actual += cargasRR[i-1][1]
                        cargasRR[i-1][1] -= cargasRR[i-1][1]
                        if(cargasRR[i-1][1] == 0 and cargasRR[i-1][0] not in cola_terminados):
                            #print(cargasRR)
                            fin = tick_actual
                            T = fin - cargasRR[i-1][2]
                            #print(T)
                            T_total += T
                            E = T - cargas[i-1][1]
                            #print(E)
                            E_total += E
                            P = T/cargas[i-1][1]
                            #print(P)
                            P_total += P
                            cola_terminados.append(cargasRR[i-1][0])
                            procesos_terminados -= 1

    T_total = T_total/len(cargasRR)
    E_total = E_total/len(cargasRR)
    P_total = P_total/len(cargasRR)
    print('RR4: T=%.2f, E=%.2f, P=%.2f' %(T_total,E_total,P_total))
    print(orden)

def spn(cargas):
    orden = ''
    i = 0
    inicio = 0
    fin = 0
    T = 0
    T_total = 0
    E = 0
    E_total = 0
    P = 0
    P_total = 0
    while i < len(cargas):
        #verificamos si es el primer elemento
        if cargas[i][2] == 0:
            orden += cargas[i][0]*cargas[i][1]
            inicio = 0
            fin = cargas[i][1]
            T = fin
            T_total += T
            E = inicio
            E_total += E
            P = T/cargas[i][1]
            P_total += P
            i += 1
        #Verificamos si llegamos al último elemento de la lista
        if i == len(cargas)-1:
            orden += cargas[i][0]*cargas[i][1]
            inicio += cargas[i-1][1]
            fin = inicio + cargas[i][1]
            T = fin - cargas[i][2]
            T_total += T
            E = T - cargas[i][1]
            E_total += E
            P = T/cargas[i][1]
            P_total += P
            i += 1
        #Comprobamos que el siguiente tenga una duración más corta
        elif(cargas[i+1][1] < cargas[i][1]):
            orden += cargas[i+1][0]*cargas[i+1][1]
            inicio += cargas[i-1][1]
            fin = inicio + cargas[i+1][1]
            T = fin - cargas[i+1][2]
            T_total += T
            E = T - cargas[i+1][1]
            E_total += E
            P = T/cargas[i+1][1]
            P_total += P
            
            orden += cargas[i][0]*cargas[i][1]
            inicio += cargas[i+1][1]
            fin = inicio + cargas[i][1]
            T = fin - cargas[i][2]
            T_total += T
            E = T - cargas[i][1]
            E_total += E
            P = T/cargas[i][1]
            P_total += P
            i +=2
        #Se ejecutará con normalidad el algoritmo
        else: 
            orden += cargas[i][0]*cargas[i][1]
            inicio += cargas[i-2][1]
            fin = inicio + cargas[i][1]
            T = fin - cargas[i][2]
            T_total += T
            E = T - cargas[i][1]
            E_total += E
            P = T/cargas[i][1]
            P_total += P
            i += 1
    #Calculamos los promedios
    T_total = T_total/len(cargas)
    E_total = E_total/len(cargas)
    P_total = P_total/len(cargas)
    print('SPN: T=%.2f, E=%.2f, P=%.2f' %(T_total,E_total,P_total))
    print(orden)
    print('\n')

print('============= Ejecución con los procesos de la clase =============')
cargas = [['A', 3, 0], ['B', 5, 1], ['C', 2, 3], ['D', 5, 9], ['E', 5, 12]]
print(cargas)
fifo(cargas)
rr1(cargas)
rr4(cargas)
spn(cargas)

print('Introduzca el número de cargas que desea probar:')
n = int(input())

for k in range(n):
    print('Ronda: ',k,)
    cargas_aleatorias = crear_cargas()
    fifo(cargas_aleatorias)
    #rr1(cargas_aleatorias)
    #rr4(cargas_aleatorias)
    spn(cargas_aleatorias)