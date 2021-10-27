# -*- coding: utf-8 -*-
#El bufon en el trono

from threading import Semaphore, Thread
from time import sleep
from random import randint
import config as c


N = 10 # Tolerancia de cortesanos que pasan
M = 5 # Tolerancia de cortesanos esperando

#Semaforos y variables de condicion
#Señalización
debeLevantarse = Semaphore(0) 
#'Apagador'
puedeSentarse = Semaphore(1)
#Torniquete  
puertaCortesanos = Semaphore(1) 
#Señalización
bufonSeSienta = Semaphore(0) 
#Mutex para todas las variables de condición. 
mutex = Semaphore(1) 
cortesanosPasados = 0
reyPresente = False 
bufonSentado = False 
#presentes en la sala, sin incluir al bufón
presentes = 0 
cortesanosEsperando = 0

#Variables que no sirven para concurrencia, sino para la visualización
puertaCerrada = False
reySentado = False

#Hilo del rey.
def rey():
	global presentes, reyPresente, bufonSentado, reySentado
	while(True):

		if( randint(0,5) == 0 ):

			mutex.acquire()
			presentes += 1
			reyPresente = True

			actualizarPantalla("                Ahi viene el rey!")

			#Si es el primero, adquiere el apagador
			if presentes == 1 and not bufonSentado:
				puedeSentarse.acquire()

			#Si el bufón está sentado, le indica que se levante y le ceda el trono.
			if bufonSentado:
				debeLevantarse.release()
				puedeSentarse.acquire()
				mutex.release()
			else:
				mutex.release()

			mutex.acquire()
			reySentado = True
			actualizarPantalla("                El rey se sienta en el trono.")
			mutex.release()

			sleep(randint(3,5))

			#El rey termina. Si es el último en salir, libera el apagador.
			mutex.acquire()
			presentes -= 1
			reySentado = False
			reyPresente = False

			actualizarPantalla("                El rey se levanta del trono y se va.")

			if presentes == 0:
				actualizarPantalla("                No hay moros en la costa!")
				puedeSentarse.release()
				bufonSeSienta.acquire()
			mutex.release()

		sleep(1)

#Hilo del bufón.
def bufon():

	#inicia con 2 segundos de retraso para darle variedad al inicio
	sleep(2)
	global reyPresente, bufonSentado, cortesanosPasados, cortesanosEsperando, puertaCerrada, presentes
	while(True):

		#Reinicia la cuenta de cortesanos que han pasado
		mutex.acquire()
		cortesanosPasados = 0
		actualizarPantalla("                El bufón espera pacientemente...")

		#Si no está protegido por un mutex externo
		if presentes == 0 and cortesanosEsperando != M:
			puedeSentarse.acquire()
			bufonSentado = True
			actualizarPantalla("                El bufón se sienta en el trono.")
			mutex.release()
		else:
			mutex.release()
			puedeSentarse.acquire()
			#Mutex externo
			bufonSentado = True
			actualizarPantalla("                El bufón se sienta en el trono.")
			bufonSeSienta.release()
			#Termina mutex externo

		#Espera a que le señalicen que debe levantarse.
		debeLevantarse.acquire()
		#Mutex externo
		#Sale
		actualizarPantalla("                El bufón debe levantarse!")
		bufonSentado = False 

		#Si hay cortesanos en la puerta, libera el torniquete.
		if cortesanosEsperando == M:
			puertaCerrada = False
			actualizarPantalla("                El bufón abre la puerta. >:)")
			puertaCortesanos.release()

		#Si el rey llegó, le cede el trono (solo sirve de mensaje)
		if reyPresente:
			actualizarPantalla("                El bufón cede el trono al rey.")

		#Cede el apagador.
		puedeSentarse.release()
		#Termina mutex externo


#Hilo del cortesano. 
def cortesano(id):
	global presentes, cortesanosEsperando, cortesanosPasados, bufonSentado, puertaCerrada

	mutex.acquire()
	cortesanosEsperando += 1

	#print("El cortesano %d está en la puerta. pr = %d, pa = %d, e = %d, " % (id, presentes, cortesanosPasados, cortesanosEsperando) )
	actualizarPantalla("                El cortesano "+str(id)+" está en la puerta.")

	#El cortesano está afuera de la sala. Si ya son M esperando:
	if cortesanosEsperando == M and puertaCerrada:	
		#print("Ya hay %d cortesanos esperando. Hay que abrirles la puerta!" % (M))
		actualizarPantalla('                Ya hay '+str(M)+' cortesanos esperando. Hay que abrirles la puerta!')
		#Si el bufón está sentado, se le señaliza que debe levantarse;
		#de lo contrario, se reinicia la cuenta y se libera el torniquete.
		if bufonSentado:
			debeLevantarse.release()
			puedeSentarse.acquire()
		else:
			cortesanosPasados = 0
			puertaCerrada = False
			actualizarPantalla("                El bufón abre la puerta. :(")
			puertaCortesanos.release()
	mutex.release()

	#Se pasa por el torniquete
	puertaCortesanos.acquire()
	puertaCortesanos.release()

	#Se actualiza presentes, cortesanosEsperando y cortesanosPasados. 
	#Si se es el primero en llegar y el bufón no está sentado, se adquiere al torniquete. 
	mutex.acquire()
	cortesanosEsperando -= 1
	cortesanosPasados += 1
	presentes += 1

	if presentes == 1 and not bufonSentado and cortesanosEsperando < (M-1):
		puedeSentarse.acquire()

	actualizarPantalla("                El cortesano "+str(id)+" está en la sala.")

	#Se entra a la sala
	#Si ya han pasado N cortesanos y el bufón no se ha sentado, se cierra el torniquete. 
	if cortesanosPasados == N and not bufonSentado:
		puertaCerrada = True
		actualizarPantalla("                El bufón ya esperó demasiado. Cierra la puerta cuando nadie lo ve.")
		mutex.release()
		puertaCortesanos.acquire()
	else: 
		mutex.release()
	
	sleep(randint(5,8))

	#El cortesano sale.
	mutex.acquire()
	presentes -= 1
	actualizarPantalla("                El cortesano "+str(id)+" se retira.")
	
	#Si es el último en retirarse y el bufón no está sentado, se libera al apagador.
	if presentes == 0 and not bufonSentado:
		actualizarPantalla("                No hay moros en la costa!")
		puedeSentarse.release()
		bufonSeSienta.acquire()
	mutex.release()


#Hilo que controla la generación de hilos de cortesanos.
def llegadaCortesanos():
	i = 1
	while(True):

		#torniquete que se puede abrir o cerrar desde la interfaz de usuario
		c.pausa.acquire()
		c.pausa.release()

		#Cada segundo hay una probabilidad de 1/2 de que llegue un cortesano
		if(randint(0,2) == 0):
			Thread(target = cortesano, args = [i]).start()
			i += 1
		sleep(1)


#Método que actualiza el estado de los actores en la pantalla
#Recibe como parámetro la descripción textual del último evento.
def actualizarPantalla(msg):

	global puertaCerrada, reyPresente, reySentado, bufonSentado, presentes

	c.grafico[0] = "  " + ("""
        Cortesano esperando
                 o
                 V 
                 Λ
                                  """*cortesanosEsperando) + (" "*(20-cortesanosEsperando))
	
	if puertaCerrada:
		c.grafico[1] = "o====================o" 
	else:
		c.grafico[1] = "o=  =================o"

	if reyPresente:
		if reySentado:
			c.grafico[2] = "|       |  K  |       "
		else: 
			c.grafico[2] = "|       |     |      K"
	else: 
		c.grafico[2] = "|       |     |       "

	if bufonSentado:
		c.grafico[3] = "|       |__B__|      |"
	else:
		c.grafico[3] = "|       |_____|   B  |"

	cortesanosPresentes = presentes
	if reyPresente:
		cortesanosPresentes -= 1
	c.grafico[5] = "| " + (cortesanosPresentes*"C") + ((19-cortesanosPresentes)*" ") + "|"
	
	c.grafico[7] = msg


	#Señalizar y esperar a que se refresque la pantalla
	c.sigHilos.release()
	c.sigInterfaz.acquire()