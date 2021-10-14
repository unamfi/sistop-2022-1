#Condiciones iniciales del problema:

#-Los gatos pueden comer de sus m platos de comida: listo
#-Los ratones pueden comer de esos mismos platos siempre y cuando no sean vistos: listo
#-Si un gato ve a un ratón comiendo, se lo debe de comer: listo
#-Los platos están puestos uno después del otro: listo
#	-Solo un animal puede comer del mismo plato: listo
#	-Si un gato está comiendo y un ratón comienza a comer de otro plato, el gato se lo debe de comer: listo
#	-Por caballerosidad los gatos no se acercan cuando los ratones comen: listo


from threading import Semaphore, Thread, Event
from time import sleep
from random import random 

entrar_a_comer = Semaphore(1)
mutexR = Semaphore(1)
mutexG = Semaphore(1)

cats = 0
rats = 0

def ratones(id,m):
	global r,cats,rats,platos
	while r!=0:
		sleep(random())
		entrar_a_comer.acquire()
		entrar_a_comer.release()

		mutexR.acquire()
		if cats>0:
			print("------>Raton:{} se lo comieron".format(id))
			r -=1
			if(r == 0):
				print("####################################################")
				print("----------SE HAN EXTERMINADO A LOS RATONES----------")
				print("####################################################")
			mutexR.release()
		
		else:
			platos[id%m].acquire()

			print("Raton:{} comienza a comer en el plato:{}".format(id,id%m))
			rats+=1

			print("Raton:{} termino de comer".format(id))
			rats-=1

			platos[id%m].release()
			mutexR.release()

def gatos(id,m):
	global r,cats,rats,platos
	while r!=0:
		sleep(random())
		entrar_a_comer.acquire()
		entrar_a_comer.release()

		mutexG.acquire()
		if rats>0:
			print("Gato:{} no se acerca a los platos por ser un caballero".format(id))
			mutexG.release()

		else:
			platos[id%m].acquire()

			print("Gato:{} comienza a comer en el plato:{}".format(id,id%m))
			cats +=1

			print("Gato:{} termino de comer".format(id))
			cats -=1

			platos[id%m].release()
			mutexG.release()

print("Inserta la cantidad de gatos:")
g = int(input())
print("Inserta la cantidad de ratones:")
r = int(input())
print("Inserta la cantidad de platos:")
p = int(input())

platos=[]

if p > 0:
	for i in range(p):
		platos.append(Semaphore(1))

	for i in range(r):
		Thread(target=ratones,args=[i,p]).start()
		
	for i in range(g):
		Thread(target=gatos,args=[i,p]).start()

else:
	print("Nadie come, ni será comido, no hay donde comer")