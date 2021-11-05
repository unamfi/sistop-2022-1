# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:11:50 2021

@author: RGJG
"""
from random import randint

def procesos():
    inicio=0
    procesos = ['A','B','C','D','E']
    #Tenemos a los procesos, ahora falta tenerlos con sus respectivos 
    #datos asi que inicializamos otra lista para despues llenarla
    procesos_info = []
    for i in range(5):
        t=randint(1,8)
        procesos_info.append([procesos[i],inicio,t])
        inicio = inicio + randint(0,t-1)
    return procesos_info

def Espera(T,tabla):
    E = []
    for i in range(5):
        E.append(T[i]-tabla[i][2])
    return E
        
def Penalizacion(T,tabla):
    P = []
    for i in range (5):
        P.append(T[i]/tabla[i][2])
    return P

def calcularPromedios(T,E,P):
    eProm = 0
    tProm = 0
    pProm = 0
    for i in range (5):
        tProm = tProm + T[i]
        eProm = eProm + E[i]
        pProm = pProm + P[i]
    #Calculo de los promedios
    tProm = round(tProm/5,2)
    eProm = round(eProm/5,2)
    pProm = round(pProm/5,2)
    return tProm,eProm,pProm
        
def cadenaS(tabla):
    #Para FIFO
    tA = 'A'*tabla[0][2]
    tB = 'B'*tabla[1][2]
    tC = 'C'*tabla[2][2]
    tD = 'D'*tabla[3][2]
    tE = 'E'*tabla[4][2]   
    cadena = tA + tB + tC + tD + tE   
    return cadena

def FIFO(tabla,cadena):
    E = []
    T = []
    P = []
    aux = 0
    aux1 = 0
    aux2 = 0
    tTotal = 0
    eProm = 0
    tProm = 0
    pProm = 0
    i=0
    for i in range(5):
        #Nos sirve para saber el tiempo de espera
        aux = tTotal-tabla[i][1]
        #Se suma el tiempo de ejecucion total
        tTotal = tTotal + tabla[i][2]
        #Tiempo de respuesta
        aux1 = tabla[i][2] + aux
        #Proporción de penalización
        aux2 = aux1/tabla[i][2]
        T.append(aux1)
        E.append(aux)
        P.append(aux2)
    #Calculo de los promedios
    promedios =calcularPromedios(T, E, P)
    tProm = promedios[0]
    eProm = promedios[1]
    pProm = promedios[2]
    print("""
          A: {}, t = {} │ B: {}, t = {} │ C: {}, t = {} │ D: {}, t = {} │ E: {}, t = {}
          (total: {})""".format(tabla[0][1],tabla[0][2],tabla[1][1],tabla[1][2],tabla[2][1],
          tabla[2][2],tabla[3][1],tabla[3][2],tabla[4][1],tabla[4][2],tTotal))
    print("""          FCFS/FIFO:   T = {} E = {} P = {}
          {}""".format(tProm,eProm,pProm,cadena))
    return 

def RR(tabla):
    #quantum = 1
    q = 1
    #Lista con los tiempos
    aux = []
    #Suma de tiempos
    st = tabla[0][2]+ tabla[1][2]+tabla[2][2]+tabla[3][2]+ tabla[4][2]
    #st = tTotal
    #Arreglo de procesos auxiliar
    RR = []
    orden = 0
    #Tiempo de respuesta
    T = []
    ta = 0
    tb = 0
    tc = 0
    td = 0
    te = 0
    for i in range(5):
        #Lista con los tiempos 
        aux.append(tabla[i][2])
    for j in range (st):
        for i in range (5):
            #Hay que controlar el orden de los procesos
            if (aux[i]>=1  and orden>=tabla[i][1]):
                #Ingresará los procesos
                RR.append(tabla[i][0])
                aux[i] = aux[i] - q
                orden = orden + 1

    #Para el calculo del tiempo de respuesta (T)
    #T = tiempo de ejecucion + tiempo de espera
    #T = t + E
    #print(RR)
    for  i in range (st):
        if(RR[i] == 'A'):
            ta = i+1
        elif (RR[i] == 'B'):
            tb = i+1
        elif (RR[i] == 'C'):
            tc = i+1
        elif (RR[i] == 'D'):
            td = i+1
        else:
            te = i+1
    #print("ta = {} │ tb = {} │ tc = {} │ td = {} │te = {}".format(ta,tb,tc,td,te))
    
    #Cantidad del proceso - Inicio
    T.append(ta-tabla[0][1])
    T.append(tb-tabla[1][1])
    T.append(tc-tabla[2][1])
    T.append(td-tabla[3][1])
    T.append(te-tabla[4][1])
    E = Espera(T, tabla)
    P = Penalizacion(T, tabla)
    #Calculo de los promedios
    promedios = calcularPromedios(T, E, P)
    tProm = promedios[0]
    eProm = promedios[1]
    pProm = promedios[2]
    #Para RR ilustrando cadena
    cadena = ''.join(RR)
    print("""          Round Robin: T = {} E = {} P = {}
          {}""".format(tProm,eProm,pProm,cadena))
    return RR, T, E, P

def SPN(tabla):
    cadena = ''
    T = []
    aux = []
    #Tiempo total
    tTotal = []
    #Orden de los procesos cortos.
    ordCortos = []
    #Asegurar al proceso A como el primero.
    ordCortos.append(tabla[0])
    #Sacamos al primer proceso de la tabla.
    tabla.pop(0)
    #Ordenamos a partir del primer proceso para saber
    #cual es el mas corto.
    tabla.sort(key=lambda x: x[2])
    for i in range(4):
        #Ya ordenados se agregan a los procesos cortos 
        ordCortos.append(tabla[i])
    for i in range (5):
        #Verificar si se trata del primer proceso
        if i == 0:
            #Agregamos a la lista el valor del tiempo que requiere el primer proceso 
            tTotal.append(ordCortos[i][2])
        else:
            tTotal.append(tTotal[i-1]+ordCortos[i][2])
        #Tiempo de respuesta por proceso
        T.append(tTotal[i]-ordCortos[i][1])
    #Cantidad del proceso - Inicio
    E = Espera(T, ordCortos)
    P = Penalizacion(T, ordCortos)
    #Calculo de los promedios
    promedios = calcularPromedios(T, E, P)
    tProm = promedios[0]
    eProm = promedios[1]
    pProm = promedios[2]
    #Para RR ilustrando cadena
    for i in range(5):
        #Hay que agregar el caracter a un arreglo para luego multiplicar de acuerdo al orden
        aux.append(ordCortos[i][0])
        #aux contiene el caracter ahora hay que multiplicarlo para la ilustracion
        cadena = cadena + aux[i]*ordCortos[i][2]
    print("""          SPN:         T = {} E = {} P = {}
          {}
          """.format(tProm,eProm,pProm,cadena))
    pass

def main ():
    rondas=['Primera', 'Segunda', 'Tercera', 'Cuarta','Quinta']
    #Numero de rondas (n)
    n=4
    for i in range(n):
        print("""         ___________________________________________________
          - {} ronda:""".format(rondas[i]))
        #Todos requieren de la tabla
        tabla = procesos()
        #A FIFO le mandamos la cadena ilustrativa
        cadenaFIFO = cadenaS(tabla)
        FIFO(tabla, cadenaFIFO)
        #Round Robin
        RR(tabla)
        #SPN
        SPN(tabla)
        print("""         ___________________________________________________""")
    return

main()




