#!/usr/bin/python3

"""
Práctica 3
Antonio Reyes Guerrero
El programa genera hilos y regresa el nombre de estos conforme son creaados
y utilizados.
Uso el comando python -m compileall para generar una carpeta __pycache__ y dentro un .pyc 
--------------------------
Código tomado de  Genbeta:
Title: Multiprocesamiento en Python: Threads a fondo, introducción
Date: 22 de septiembre, 2011
Title of program: 
Code version:
Type: source code
Availability:
https://www.genbeta.com/desarrollo/multiprocesamiento-en-python-threads-a-fondo-introduccion 
"""
import threading
import time

def worker():
	"""Obtiene el nombre del hilo creado, puede tener un nombre o uno determinado """
	print(threading.currentThread().getName(),'Lanzado')
	time.sleep(2)
	print(threading.currentThread().getName(),'Deteniendo')

def servicio():
	print(threading.currentThread().getName(),'Lanzado')
	print(threading.currentThread().getName(),'Deteniendo')

#Instanciando los hilos

t = threading.Thread(target=servicio,name='Servicio')
w = threading.Thread(target=worker,name='Worker')
z = threading.Thread(target=worker)

#Ejercucion de los hilos

w.start()
z.start()
t.start()
