#!/usr/bin/python3
import threading
from time import sleep

datos = []
for i in range(10000):
    datos.append(i)

def duplica(arreglo, base, cuantos):
    for i in range(cuantos):
        arreglo[base + i] = arreglo[base + i] * 2

for segmento in range(100):
    hilo = threading.Thread(target=duplica, args=[datos, segmento*100, 100])
    hilo.start()

# sleep(2)
print('Los primeros valores son: %d, %d, %d, %d, %d' %
      (datos[0], datos[1], datos[2], datos[3], datos[4]))
print('Los últimos valores son: %d, %d, %d, %d, %d' %
      (datos[-1], datos[-2], datos[-3], datos[-4], datos[-5]))
