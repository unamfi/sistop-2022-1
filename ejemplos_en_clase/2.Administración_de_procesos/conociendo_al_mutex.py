#!/usr/bin/python3
import time
import threading
l = threading.Lock()

def usando_mutex(num):
    time.sleep(0.01)
    global l
    print('%d entrando a la función' % num)
    l.acquire()
    print('%d tiene la ejecución!' % num)
    time.sleep(0.5)
    l.release()
    print('%d ya terminó' % num)

def otro_ruidoso():
    for i in range(10):
        print('...')
        time.sleep(1)

threading.Thread(target=otro_ruidoso).start()
for i in range(15):
    threading.Thread(target=usando_mutex, args=[i]).start()
