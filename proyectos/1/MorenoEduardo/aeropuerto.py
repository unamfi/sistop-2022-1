#!/usr/bin/python3
# @author: Eduardo Peralta
# 
# Problema

#El problema del aeropuerto, o mas bien el problema de la cinta transportado de maletas.
import threading
import time
import random
import sys
import os 
#Variables:

num_maletas = 0
limite_maletas = False
num_pasajeros = 0
limite_pasajeros = False
num_hack = 0    
num_serf = 0    

maletas_ = threading.Semaphore(0)  #💼
pasajeros_ = threading.Semaphore(0) #👤

mutex_ingreso = threading.Semaphore(3)
mutex_maletas = threading.Semaphore(2)
mutex_pasajeros = threading.Semaphore(2)
mutex_recoger = threading.Semaphore(2)


def maletas():
    global num_maletas
    global mutex_maletas
    global limite_pasajeros
    global limite_maletas
    global maletas_

    mutex_maletas.acquire()

    if (num_maletas == 15 and limite_maletas==False):
        limite_maletas = True
        mutex_maletas.release()
    elif (num_maletas >= 7 and num_maletas < 15 ):
        num_maletas += 1
        print("Ha llegado ", end="")
        ingresa("maleta")
        print("")
        
        #ingresa("maleta")
        #pantalla()
        
        mutex_maletas.release()
        #
    else:
        if(limite_maletas == False):
            num_maletas += 1
            print("Ha llegado ", end="")
            ingresa("maleta")
            print("")
            mutex_maletas.release()
            maletas_.acquire()
        elif(limite_maletas == False and num_maletas != 15):
            limite_maletas = True
        else:
            mutex_maletas.release()
            print("¡No hay espacio en la cinta!")

def pasajeros(recoge):
    global num_pasajeros
    global limite_maletas
    global limite_pasajeros
    global mutex_pasajeros
    global pasajeros_
    global maletas_

    mutex_pasajeros.acquire()

    if (num_pasajeros == 20 and limite_pasajeros == False):
        limite_pasajeros = True
        mutex_pasajeros.release()
    elif (num_pasajeros >= 7 and num_pasajeros <= 20 and recoge == 1):
           
        #ingresa("pasajero")
        #pantalla()
        pasajeros_.release()
        maletas_.release()
        mutex_pasajeros.release()
        recoger()
        
    else:
        if(limite_pasajeros == False):
            num_pasajeros += 1
            print("Ha llegado ", end="")
            ingresa("pasajero")
            print("")
            mutex_pasajeros.release()
            pasajeros_.acquire()
        elif(limite_pasajeros == False and num_maletas !=20):
            limite_pasajeros == True
        else:
            mutex_pasajeros.release()
            print("¡No hay espacio alrededor de la cinta!")
        
    

def ingresa(tipo):
    
    if(tipo == "maleta"):
        print("💼", end="")
    elif(tipo == "pasajero"):
        print("👤", end="")
    

def borrarPantalla(): #Borra pantalla dependiendo del sistema operativo
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def imprimirProblema():
    print("                         ======== La cinta del aeropuerto ========               ")
    print("Nos encontramos en un aeropuerto, en el aeropuerto tenemos una cinta que trae el equipaje,"
    + " alrededor de ella hay gente esperando para recogerlo, pasa el tiempo, entra y sale equipaje, así como personas, no todo" +
    " el equipaje saldrá, pero observemos como se mueve el ritmo de maletas en el aeropuerto")

def recoger():
    global num_maletas
    global num_pasajeros
    global limite_maletas
    global limite_pasajeros
    mutex_recoger.acquire()

    num_maletas = num_maletas -1
    num_pasajeros = num_pasajeros -1
    if (num_pasajeros == 0 or num_maletas == 0):
        print("No hay nada")
    elif(num_pasajeros >= 1 and num_maletas >= 1):
        print("Se va ", end="")
        ingresa("pasajero")
        print("")
        print("Se va ", end="")
        ingresa("maleta")
        print("")
    else:
        print("Todo mal")
    mutex_recoger.release()

def pantalla():
    global num_pasajeros
    global num_maletas
    a = 0
    b = 0
    mutex_ingreso.acquire()
    while a < num_maletas: 
        ingresa("maleta")
        a += 1
    print(" ")
    while b < num_pasajeros:
        ingresa("pasajero")
        b += 1 
    
    
    mutex_ingreso.release()


try:
    while True:
        #
        #borrarPantalla()
        #
        #imprimirProblema()
        #
        if round(random.choice([0,1])) == 0:
            threading.Thread(target = maletas, args = []).start()
            time.sleep(2)
            pantalla()
            print(threading.active_count())
        else:
            threading.Thread(target = pasajeros, args = [round(random.choice([0,1]))]).start()
            time.sleep(2)
            pantalla()
            #time.sleep(2)
            print(threading.active_count())

        #
except KeyboardInterrupt:
    print("             ║║ Vámonos a casa ║║               ")
    
    sys.exit()
except AttributeError:
    sys.exit()