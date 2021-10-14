#!/usr/bin/python3
from threading import Semaphore, Thread
import time

s = Semaphore(0)

def ahora_con_semaforo(num):
    global s
    print('%d entrando a la función' % num)
    s.acquire()
    print('%d tiene el semáforo - Estoy dentro!' % num)
    time.sleep(0.5)
    s.release()
    print('%d salió del semáforo' % num)

for i in range(15):
    Thread(target=ahora_con_semaforo, args=[i]).start()

time.sleep(3)
s.release()
