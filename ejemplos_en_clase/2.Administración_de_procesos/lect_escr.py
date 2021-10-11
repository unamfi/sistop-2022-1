#!/usr/bin/python3

import time
import random
import threading

lectores = 0
mutex = threading.Semaphore(1)
cuarto_vacio = threading.Semaphore(1)
quiero_entrar = threading.Semaphore(1)

def escritor(num):
    while True:
        time.sleep(random.random())
        quiero_entrar.acquire()
        cuarto_vacio.acquire()
        escribe(num)
        cuarto_vacio.release()
        quiero_entrar.release()

def lector(num):
    global lectores
    while True:
        time.sleep(random.random())
        quiero_entrar.acquire()
        quiero_entrar.release()

        mutex.acquire()
        lectores = lectores + 1
        if lectores == 1:
            cuarto_vacio.acquire()
            print('Lector %d adquiere el cuarto' % num)
        mutex.release()

        lee(num)

        mutex.acquire()
        lectores = lectores - 1
        if lectores == 0:
            print('Lector %d libera el cuarto' % num)
            cuarto_vacio.release()
        mutex.release()

def lee(num):
    print('Lector %d entra a leer' % num)
    time.sleep(random.random())
    print('Lector %d terminó.' % num)

def escribe(num):
    print('Escritor %d entra a escribir' % num)
    time.sleep(random.random())
    print('Escritor %d terminó.' % num)

for i in range(2):
    threading.Thread(target=escritor, args=[i]).start()

for i in range(10):
    threading.Thread(target=lector, args=[i]).start()
