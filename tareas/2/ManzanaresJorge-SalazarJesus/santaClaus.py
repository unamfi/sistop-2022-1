#!/usr/bin/python3
import time
import threading
import random

#Variables globales
num_duendes = 10
duendes_tristes = 0
renos_puntuales = 0
lista_duendes_tristes = []

#Semáforos utilizados
mutex_duende = threading.Semaphore(1)
mutex_reno = threading.Semaphore(1)
duende_atorado = threading.Semaphore(0)
reno_en_casa = threading.Semaphore(0)


#Definición de Santa Claus
def Santa():
    global duendes_tristes, renos_puntuales
    while True:
        while(duendes_tristes < 3 and renos_puntuales < 9):
            pass

        #Ayuda a los duendes
        if(duendes_tristes >= 3):
            print("S: Duendes liberados: (%d, %d, %d)" %(lista_duendes_tristes[0], lista_duendes_tristes[1], lista_duendes_tristes[2]))
            for k in range(3):
                duende_atorado.release()
                lista_duendes_tristes.pop()
            duendes_tristes = duendes_tristes - 3

        #Ayuda a los renos
        if(renos_puntuales == 9):
            print("S: Santa se fue de viaje con los renos")
            for k in range(9):
                reno_en_casa.release()
            renos_puntuales = 0


#Definición de duende
def Duende(id_duende):
    global duendes_tristes, mutex_duende
    while True:
        print("D: Duende %d trabajando" %id_duende)
        time.sleep(random.random())

        #Sección crítica de duendes
        mutex_duende.acquire()
        duendes_tristes = duendes_tristes + 1
        lista_duendes_tristes.append(id_duende)
        print("D: ¡Duende %d atorado!" %id_duende)
        mutex_duende.release()
        duende_atorado.acquire()


#Definición de reno
def Reno(id_reno):
    global renos_puntuales, mutex_reno
    while True:
        time.sleep(random.random())

        #Sección crítica de renos
        mutex_reno.acquire()
        renos_puntuales = renos_puntuales + 1
        print("R: ¡Reno %d listo para santa!" %id_reno)
        mutex_reno.release()
        reno_en_casa.acquire()


#Creando el hilo de Santa
threading.Thread(target=Santa,args=[]).start()

#Creando los hilos de duendes
for i in range (num_duendes):
    threading.Thread(target=Duende,args=[i]).start()

#Creando los hilos de renos
for j in range(9):
    threading.Thread(target=Reno,args=[j]).start()
