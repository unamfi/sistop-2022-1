import threading
import time
import random

x = 5 #número de sillas
alumno = threading.Semaphore(0)
salon = threading.Semaphore(0)
profeOcupado = threading.Semaphore(1)
numIn = 0
i = 0

def alumnos():
	global alumno
	while True:
		time.sleep(random.random() / 3.0)
		for i in range (3):
			print('   A: Tengo dudas')
			alumno.release()

def profesor():
	global alumno
	if (numIn > 0): #se acabó la siesta :(
		print ('P: Ya me desperté')
		print('El número de alumnos es: ', numIn)
		profeOcupado.acquire()
		alumno.acquire()
		print('P: Contestaré tus preguntas')
		print('P: Terminé con tus dudas, suerte')
		profeOcupado.release()


def entra():
	global numIn, alumno
	while True:
		alumno.acquire()
		if (numIn < x+1):
			alumno.release()
			numIn += 1
			profesor()
			

threading.Thread(target=entra, args=[]).start()
threading.Thread(target=alumnos, args=[]).start()
