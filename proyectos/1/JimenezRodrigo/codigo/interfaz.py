# -*- coding: utf-8 -*-
import curses
from time import sleep
import proyecto as pyt
import config as c
from threading import Semaphore, Thread


def menu():
	#Se inicia pantalla, se obtienen dimensiones de la consola
	scr = curses.initscr()
	curses.noecho()
	dims = scr.getmaxyx() 

	hilosCorriendo = False

	q = -1
	while q != 113 and q != 81:
		
		scr.nodelay(1)
		q = scr.getch()

		scr.clear()
		#Pantalla de titulo
		scr.addstr(1,dims[1]-24, 'Presione \'q\' para salir')
		scr.addstr(2,(dims[1]-39)//2,' _____ _   _            __            ') 
		scr.addstr(3,(dims[1]-39)//2,'|  ___| | | |          / _|           ')
		scr.addstr(4,(dims[1]-39)//2,'| |__ | | | |__  _   _| |_ ___  _ __  ')
		scr.addstr(5,(dims[1]-39)//2,'|  __|| | | \'_ \\| | | |  _/ _ \\| \'_ \\ ')
		scr.addstr(6,(dims[1]-39)//2,'| |___| | | |_) | |_| | || (_) | | | |')
		scr.addstr(7,(dims[1]-39)//2,'\\____/|_| |_.__/ \\__,_|_| \\___/|_| |_|')

		scr.addstr(8,(dims[1]-50)//2,'                   _   _                         \n')
		scr.addstr(9,(dims[1]-50)//2,'                  | | | |                        \n')
		scr.addstr(10,(dims[1]-50)//2,'  ___ _ __     ___| | | |_ _ __ ___  _ __   ___  \n')
		scr.addstr(11,(dims[1]-50)//2,' / _ \\ \'_ \\   / _ \\ | | __| \'__/ _ \\| \'_ \\ / _ \\ \n')
		scr.addstr(12,(dims[1]-50)//2,'|  __/ | | | |  __/ | | |_| | | (_) | | | | (_) |\n')
		scr.addstr(13,(dims[1]-50)//2,' \\___|_| |_|  \\___|_|  \\__|_|  \\___/|_| |_|\\___/ \n')

		scr.addstr(16,(dims[1]//2)-15,'1. El problema')
		scr.addstr(18,(dims[1]//2)-15,"""2. Ejecución visual
             Opcion:""")
        
		scr.refresh()
		
		s = -1

		#1. El problema
		if q == 49:
			scr.clear()
			scr.nodelay(1)
			#Mostrar la descripcion del problema hasta salir.
			while s != 115 and s != 83:
				scr.addstr(1, dims[1]-33,'Presiona \'s\' parar salir al menú')
				scr.addstr(2, (dims[1]-20)//2,'El bufón en el trono')
				scr.addstr(3, 2,"""
               El bufón de la corte tiene un pasatiempo secreto: 
               le gusta disfrazarse del rey y sentarse en el trono. 
               Sin embargo, solo puede hacer esto cuando no hay nadie presente
               en la sala: ni el rey ni los cortesanos. 
               -El bufón aprovechará cualquier oportunidad que tenga para darse este lujo. 
               -El rey suele ausentarse por periodos considerables de tiempo, 
                mientras que varios cortesanos pueden entrar y salir de la sala.
               -Si el rey llega mientras el bufón está sentado, 
                el bufón tiene que levantarse inmediatamente y cederle el trono. 
               -Si un cortesano llega mientras el bufón está sentado, 
               pensará que es el rey y no lo molestará. 
               -El bufón también es impaciente, por lo que si cuenta que ya pasaron 10 cortesanos 
                por la sala y no lo han dejado a solas con el trono, aún en presencia del rey, cerrará maliciosamente 
                la puerta de los cortesanos y esperará a que todos se vayan. 
               -Los cortesanos tendrán que esperar afuera. Desafortunadamente, 
                cuando hay 5 cortesanos esperando, éstos se ponen impacientes, 
                y el bufón tiene abrirles la puerta, aún si no está sentado.""")

				scr.nodelay(0)
				s = scr.getch()
				scr.clear()

		#2. Ejecucion visual
		elif q == 50:

			scr.clear()
			scr.nodelay(1)

			#Lista de los últimos 10 eventos
			textoEntrante = [""]*10

			#Se crean y se inician los hilos la primera vez que se entra aquí
			if not hilosCorriendo:
				hiloRey = Thread(target = pyt.rey, args = [])
				hiloBufon = Thread(target = pyt.bufon, args = [])
				hiloCortesanos = Thread(target = pyt.llegadaCortesanos, args = [])
				hiloRey.start()
				hiloBufon.start()
				hiloCortesanos.start()
				hilosCorriendo = True

			#Se abre el torniquete para generar cortesanos
			c.pausa.release()
			while s != 115 and s != 83:
				s = scr.getch()

				#Se espera a que un hilo avise de una actualización
				c.sigHilos.acquire()
				scr.clear()

				#Se visualiza el estado actual del escenario
				scr.addstr(1, dims[1]-33,'Presiona \'s\' parar salir al menú')
				scr.addstr(2,(dims[1]-20)//2,"El bufón en el trono") 
				scr.addstr(4,(dims[1]-23)//2,c.grafico[0]) 
				scr.addstr(5,(dims[1]-23)//2,c.grafico[1])
				scr.addstr(6,(dims[1]-23)//2,c.grafico[2]) 
				scr.addstr(7,(dims[1]-23)//2,c.grafico[3])
				scr.addstr(8,(dims[1]-23)//2,c.grafico[4])
				scr.addstr(9,(dims[1]-23)//2,c.grafico[5])
				scr.addstr(10,(dims[1]-23)//2,c.grafico[6])
				scr.addstr(12,(dims[1]-31)//2,"B-Bufon    C-Cortesano    K-Rey")

				#Se actualiza la lista de eventos recientes, y se muestra
				for i in reversed(range(9)):
					textoEntrante[i+1] = textoEntrante[i]
				textoEntrante[0] = c.grafico[7]

				scr.addstr(14,(dims[1]-66)//2,textoEntrante[9])
				scr.addstr(15,(dims[1]-66)//2,textoEntrante[8])
				scr.addstr(16,(dims[1]-66)//2,textoEntrante[7])
				scr.addstr(17,(dims[1]-66)//2,textoEntrante[6])
				scr.addstr(18,(dims[1]-66)//2,textoEntrante[5])
				scr.addstr(19,(dims[1]-66)//2,textoEntrante[4])
				scr.addstr(20,(dims[1]-66)//2,textoEntrante[3])
				scr.addstr(21,(dims[1]-66)//2,textoEntrante[2])
				scr.addstr(22,(dims[1]-66)//2,textoEntrante[1])
				scr.addstr(23,(dims[1]-66)//2,textoEntrante[0]) 
				scr.refresh()
				sleep(0.25)

				#Se señaliza al actor que ya se termino de actualizar la pantalla.
				c.sigInterfaz.release()

			#Se cierra el torniquete para detener la generación de cortesanos
			c.pausa.acquire()

		sleep(0.05)

	curses.endwin()


menu()