#!/usr/bin/python3
from threading import Semaphore, Thread
import time
import random

cuenta = 0
mut_cuenta = Semaphore(1)
barrera = Semaphore(1)
espera_a = 5

def vamos(id):
    global cuenta, mut_cuenta, barrera, espera_a
    print('%d: Iniciando' % id)
    time.sleep(random.random())
    print('%d Listo! cuenta = %d' % (id, cuenta))
    mut_cuenta.acquire()
    # si soy el primero, bajo la barrera
    if cuenta == 0:
        barrera.acquire()
    # Aumento la cuenta
    cuenta = cuenta + 1
    # Si soy el último, subo la barrera
    if cuenta == espera_a:
        barrera.release()
        cuenta = 0
    mut_cuenta.release()
    barrera.acquire()
    barrera.release()
    print('%d pasó la barrera!' % id)

for i in range(30):
    Thread(target=vamos, args=[i]).start()
