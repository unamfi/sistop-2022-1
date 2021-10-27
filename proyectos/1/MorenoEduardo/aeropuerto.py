#!/usr/bin/python3
# @author: Eduardo Peralta
# 
# Problema

#El problema del aeropuerto, o mas bien el problema de la cinta transportado de maletas.
import threading
import time
import random
import sys

#Variables:

num_maletas = 0
limite_maletas = False
num_pasajeros = 0
limite_pasajeros = False
num_hack = 0    
num_serf = 0    

maletas_ = threading.Semaphore(0)  #💼
pasajeros_ = threading.Semaphore(0) #👤

mutex_ingreso = threading.Semaphore(1)
mutex_maletas = threading.Semaphore(1)
mutex_pasajeros = threading.Semaphore(1)
mutex_recoger = threading.Semaphore(2)


def maletas():
    global num_maletas
    global mutex_maletas
    global limite_pasajeros

    mutex_maletas.acquire()

    if (maletas == 15):
        limite_maletas = True
        mutex_maletas.release()
    elif (num_maletas >= 0 and num_maletas < 15 ):
        num_maletas += 1
        mutex_maletas.release()
        ingresa("maleta")
        maletas_.acquire()
        
    else:
        print("Algo anda mal (maletas)")
        mutex_maletas.release()


def pasajeros():
    global num_pasajeros
    global limite_maletas
    global mutex_pasajeros

    mutex_pasajeros.acquire()

    if (maletas == 20):
        limite_pasajeros = True
        mutex_pasajeros.release()
    elif (num_pasajeros >= 0 and num_pasajeros < 20 ):
        num_pasajeros += 1
        mutex_pasajeros.release()
        ingresa("pasajero")
        pasajeros_.acquire()
        
    else:
        print("Algo anda mal (pasajeros)")
        mutex_pasajeros.release()

def ingresa(tipo):
    mutex_ingreso.acquire()
    if(tipo == "maleta"):
        print("💼")
    elif(tipo == "pasajero"):
        print("👤")
    mutex_ingreso.release()

def borrarPantalla(): #Borra pantalla dependiendo del sistema operativo
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def imprimirProblema():
    print("======== La cinta del aeropuerto ========")
    print("Nos encontramos en un aeropuerto, en el aeropuerto tenemos una cinta que trae el equipaje,"
    + " alrededor de ella hay gente esperando para recogerlo, pasa el tiempo, entra y sale equipaje, así como personas, no todo" +
    " el equipaje saldrá, pero observemos como se mueve el ritmo de maletas en el aeropuerto")

def recoger(desarrollador,icon):
    global num_maletas
    global num_pasajeros
    global limite_maletas
    global limite_pasajeros
    mutex_recoger.acquire()

    if (num_pasajeros == 0 or num_maletas == 0):
        print("No hay nada")
    
    mutex_recoger.release()




try:
    while True:
        if round(random.choice([0,1])) == 0:
            threading.Thread(target = maletas, args = []).start()
            time.sleep(0.5)
            print(threading.active_count())
        else:
            threading.Thread(target = pasajeros, args = []).start()
            time.sleep(0.5)
            print(threading.active_count())


except KeyboardInterrupt:
    print("║║ Vámonos a casa ║║")
    sys.exit()