# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:50:45 2021

@author: Carlo
"""

import random
import copy
class Proceso:
    def __init__(self,lista,i):
        self.letra=lista[i]#Procesos
        self.tiempo=random.randint(1, 10)#Tiempo de ejecucion
        self.tiempoinicial=random.randint(0, self.tiempo-1)#Tiempo inicio
        #self.prioridad=i+1#random.randint(0, 4)
#Ordenamos nuestros proceso con respecto al tiempo inicial
def ordenamiento(lista):
    c=[]
    anterior=0
    for j in lista:
        if j.tiempoinicial==0:
            obj=j
            c.insert(0,obj)
            #palabra=palabra+str(j.letra*j.tiempo)
        else:
            if j.tiempoinicial>anterior:
                obj=j
                c.append(obj)
             #   palabra=palabra+str(j.letra*j.tiempo)
                anterior=j.tiempoinicial
            else:
                obj=j
                c.insert(1,obj)
              #  palabra=palabra+str(j.letra*j.tiempo)
                anterior=j.tiempoinicial
    return c
def fifo(priori):
    #c=copy.deepcopy(priori)
    palabra=""
    #c=[]
    T=0
    E=0
    P=1
    for k in c:
        T=(T+k.tiempo)-k.tiempoinicial
        E=E+(T-k.tiempo)
        P=P+(T/k.tiempo)
        #T=T+k.tiempo
    for n in c:
        palabra=palabra+str(n.letra*n.tiempo)
    print("FIFO")
    print(palabra)#Se ordena con respecto al orden previo de tiempo inicial
    T1=T/len(num_procesos)
    E1=E/len(num_procesos)
    P1=P/len(num_procesos)
    print("T =",T1," E =",E1,"P =",P1)
def rr(lista):
    procesos_eje=[]
    T=0
    E=0
    P=0
    palabra=""
    procesosTerminado=5
    tick=0
    copia2=lista
    copialista=copy.deepcopy(lista)
    print("RR")
    while procesosTerminado>0:
        for i in copialista:
            if i.tiempoinicial<=tick and i.tiempo>0 :
                palabra=palabra+str(i.letra)
                #print(palabra)
                i.tiempo=i.tiempo-1
                tick +=1
            if i.tiempo==0 and i.letra not in  procesos_eje :
                procesos_eje.append(i.letra)
                procesosTerminado-=1
    for r in copia2:
        #print(r.tiempo)
        T=(T+r.tiempo)-r.tiempoinicial
        E=E+(T-r.tiempo)
        P=P+(T/r.tiempo)
    T1=T/len(num_procesos)
    E1=E/len(num_procesos)
    P1=P/len(num_procesos)
    print(palabra)
    print("T=",T1,"E=",E1,"P",P1)
def spn(lista):
    #tiempos=[]
    T=0
    E=0
    P=0
    ejecucion=[]
    espera=[]
    palabra=""
    copia=lista.copy()
    for l in copia:
           tiempos=[]
           tiempos.append(l.tiempoinicial)
           tiempos.append(l.tiempo)
           tiempos.append(l.letra)
           ejecucion.append(tiempos)
    for h in ejecucion:
        tiempo=h[0]
        if tiempo==0:
            palabra=palabra+h[1]*h[2]
            #print(palabra)
            T=(T+h[1])-h[0]
            E=E+(T-h[1])
            P=P+(T/h[1])
            #print(T)
        else:
            espera.append(h[1])
            T=(T+h[1])-h[0]
            E=E+(T-h[1])
            P=P+(T/h[1])
            #palabra=palabra+(h[1]*h[2])
            #print(T)
            espera.append(h[2])
    num=espera[0]
    for w in range(0,len(espera)):#Se va comparando tiempo de ejecución
        tipo=type(espera[w])
        if tipo==int:
            if num<espera[w]:
                palabra=palabra+(espera[w]*espera[w+1])
            else:
                palabra=palabra+(espera[w]*espera[w+1])
    print("SNP")
    print(palabra)
    #print(T)
    #print(E)
    #print(P)
    t1=T/len(num_procesos)
    e1=E/len(num_procesos)
    p1=P/len(num_procesos)
    print("T=",t1, "E=",e1,"P=",p1)
orden=[]  
num_procesos=['A','B','C','D','E']
for i in range(0,len(num_procesos)):
    orden.append(Proceso(num_procesos,i))
    #orden.append(p)
c=ordenamiento(orden)
fifo(c)
rr(c)
spn(c)