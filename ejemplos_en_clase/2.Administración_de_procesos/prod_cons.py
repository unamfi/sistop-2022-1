import threading
import random
import time
buffer = []

max_elem = 5
demora_creacion = 0.2
demora_consumo = 0.3

mut_buffer = threading.Semaphore(1)
señaliza = threading.Semaphore(0)
menos_que_maximo = threading.Semaphore(max_elem)

def productor():
    while True:
        event = genera_evento()
        menos_que_maximo.acquire()
        mut_buffer.acquire()
        buffer.append(event)
        mut_buffer.release()
        señaliza.release()

def consumidor():
    while True:
        señaliza.acquire()
        mut_buffer.acquire()
        event = buffer.pop()
        mut_buffer.release()
        menos_que_maximo.release()
        procesa(event)

def genera_evento():
    elem = random.random()
    time.sleep(demora_creacion)
    print('Generando %1.3f' % elem)
    return(elem)

def procesa(elem):
    time.sleep(demora_consumo)
    print('Procesando %1.3f, hay %d elementos pendientes' % (elem, len(buffer)))

for i in range(3):
    threading.Thread(target=productor,args=[]).start()
for i in range(7):
    threading.Thread(target=consumidor,args=[]).start()
