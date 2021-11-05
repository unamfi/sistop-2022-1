import random
import copy 

#Crea la lista de procesos para cada uno de las funciones
def CrearProcesosBase():
	nombres_procesos = ['A','B','C','D','E']
	procesos = []
	tiempo_llegada = 0

	#Llena la lista de procesos, con un nombre, un tiempo de llegada y un tiempo que requiere el proceso.
	for i in range(len(nombres_procesos)):
		tiempo_requerido = random.randint(5,15)
		tiempo_llegada += random.randint(1,5)
		procesos.append([nombres_procesos[i],tiempo_llegada,tiempo_requerido])

	return procesos

#Primer algoritmo de ordenamiento.
def FCFS(procesos):

	#Listas para las métrícas
	T = [] #Tiempo total
	E = [] #Tiempo de espera
	P = [] #Penalización

	tiempo_inicio = 0
	orden_ejecucion = ''
	contador_procesos = 0

	#Como el tiempo de llegada es entre (1,5) y se acumula para facilitar el analisis, se resta el tiempo de salida del primero a cada uno, y comienza en cero.
	resta = procesos[contador_procesos][1]
	for i in range(len(procesos)):
		procesos[i][1] -= resta

	#Se recorre la lista de procesos y de forma lineal, y se calcula el tiempo de inicio del siguiente proceso, para saber el tiempo de espera del proceso
	#con respecto al tiempo en que llego
	while(contador_procesos < len(procesos)):
		for i in range(procesos[contador_procesos][2]):
			orden_ejecucion += procesos[contador_procesos][0] #Como es lineal se guardan las impresiones en el orden que estan los procesos.

		#El primer proceso no se ve afectado por lo demás procesos
		if(contador_procesos==0):
			T.append(procesos[contador_procesos][2])
			E.append(0)
			P.append(T[contador_procesos]/procesos[contador_procesos][2]) #P= T/t
			tiempo_inicio += procesos[contador_procesos][2] #Tinicio += Tiempo pedido
			contador_procesos += 1
		else:
			Tiempo_espera = tiempo_inicio - procesos[contador_procesos][1]
			T.append(procesos[contador_procesos][2] + Tiempo_espera) #Ttotal = Trequerido + Tespera
			E.append(Tiempo_espera)
			P.append(T[contador_procesos]/procesos[contador_procesos][2]) #P= Ttotal/Trequerido
			tiempo_inicio += procesos[contador_procesos][2]
			contador_procesos += 1

	#Se calcula las metricas
	TT = sum(T)/len(procesos)
	TE = sum(E)/len(procesos)
	TP = sum(P)/len(procesos)

	#Se imprimen las metricas.
	print("FCFS: T=%.2f, E=%.2f, P=%.2f"%(TT,TE,TP))
	print(orden_ejecucion)
	print(len(orden_ejecucion))

#Segundo algoritmo de ordenamiento
def RR(procesos):

	T = []
	E = []
	P = []

	tiempo_Final = []
	tiempo_requerido = []
	orden_ejecucion = ''
	tiempo_total = 0
	contador = 0

	#Se calcula el tiempo total requerido por los procesos
	for i in range(len(procesos)):
		tiempo_requerido.append(procesos[i][2])

	#Se crea una copia no cambiante de la lista original de procesos, para los demás algoritmos
	lista = copy.deepcopy(procesos)

	tiempo_total = sum(tiempo_requerido)

	while(contador < tiempo_total):
		for i in range(len(procesos)): #Por cada iteración se visita cada proceso y se verifica que tiempo de llegada del proceso
			if(contador >= procesos[i][1] and procesos[i][2] > 0): #Si el proceso puede ejecutarse porque ya llego y requiere tiempo se ejecuta una sola vez
				procesos[i][2]-=1
				orden_ejecucion += procesos[i][0]
				contador += 1
				if(procesos[i][2] == 0): #Si el proceso ya termino con sus tiempo requerido se manda a una lista para saber cuanto tiempo tardo en total
					tiempo_Final.append([procesos[i][0],contador])

	#Se ordenan los tiempos de finalizacion en base al nombre del proceso
	tiempo_Final.sort()

	#Se calculan las metrícas.
	for i in range(len(procesos)):
		T.append(tiempo_Final[i][1]-procesos[i][1]) #Ttotal=Tfinal- Tllegada 
		E.append(T[i] - tiempo_requerido[i]) #Tespera = Ttoal - Trequerido
		P.append(T[i]/tiempo_requerido[i])

	TT = sum(T)/len(procesos)
	TE = sum(E)/len(procesos)
	TP = sum(P)/len(procesos)

	print("RR: T=%.2f, E=%.2f, P=%.2f"%(TT,TE,TP))
	print(orden_ejecucion)
	print(len(orden_ejecucion))

	return lista

#Tercer algoritmo de ordenamiento
def RR4(procesos):

	T = []
	E = []
	P = []

	tiempo_Final = []
	tiempo_requerido = []
	orden_ejecucion = ''
	tiempo_total = 0
	contador = 0

	lista = copy.deepcopy(procesos)

	for i in range(len(procesos)):
		tiempo_requerido.append(procesos[i][2])

	tiempo_total = sum(tiempo_requerido)

	while(contador < tiempo_total):
		for i in range(len(procesos)):
			if(contador >= procesos[i][1] and procesos[i][2]>0): 
				if(procesos[i][2] >= 4): #Verifica que el proceso requiera mas de 4 quantums, y si cumple le quita el tiempo de 4 
					procesos[i][2] -= 4
					for R in range(4):
						orden_ejecucion += procesos[i][0]
					contador += 4
					if(procesos[i][2] == 0):
						tiempo_Final.append([procesos[i][0],contador])

				elif(procesos[i][2] < 4): #Si requiere menos tiempo, ejecuta por completo el proceso
					for R in range(procesos[i][2]):
						orden_ejecucion += procesos[i][0]
					contador += procesos[i][2]
					procesos[i][2] -= procesos[i][2]
					if(procesos[i][2] == 0):
						tiempo_Final.append([procesos[i][0],contador])

	tiempo_Final.sort()

	for i in range(len(procesos)):
		T.append(tiempo_Final[i][1]-procesos[i][1])
		E.append(T[i] - tiempo_requerido[i])
		P.append(T[i]/tiempo_requerido[i])

	TT = sum(T)/len(procesos)
	TE = sum(E)/len(procesos)
	TP = sum(P)/len(procesos)

	print("RR4: T=%.2f, E=%.2f, P=%.2f"%(TT,TE,TP))
	print(orden_ejecucion)
	print(len(orden_ejecucion))

	return lista

#Cuarto algoritmo de ordenamiento
def SPN(procesos):

	T = []
	E = []
	P = []

	lista = copy.deepcopy(procesos)

	tiempo_Final = []
	tiempo_requerido = []
	orden_ejecucion = ''
	contador = 0

	for i in range(len(procesos)):
		tiempo_requerido.append(procesos[i][2])

	for i in range(len(procesos)-1): #Compara las localidades de la lista de procesos, y al final deja el proceso que mas requiere de tiempo
		if(procesos[i][2] <= procesos[i+1][2]): #Comprueba de que el elemento actual sea menor y si loes lo ejecuta por completo
			for r in range(procesos[i][2]):
				orden_ejecucion += procesos[i][0]
			contador += procesos[i][2]
			procesos[i][2] -= procesos[i][2]
			if(procesos[i][2] == 0):
				tiempo_Final.append([procesos[i][0],contador])
		else: #En caso de que sea mayor el proceso actual ejecuta el siguiente
			for r in range(procesos[i+1][2]):
				orden_ejecucion += procesos[i+1][0]
			contador += procesos[i+1][2]
			procesos[i+1][2] -= procesos[i+1][2]
			if(procesos[i+1][2] == 0):
				tiempo_Final.append([procesos[i+1][0],contador])
			aux = procesos[i] #Como se ejecuta el siguiente proceso, se hace un intercambio de posiciones para no perder el proceso.
			procesos[i] = procesos[i+1]
			procesos[i+1] = aux

		contador_for = i #Se guarda  el valor de ultima posición que no se comprueba

	#Se ejecuta el ultimo proceso
	for r in range(procesos[contador_for+1][2]):
		orden_ejecucion += procesos[contador_for+1][0]
	contador += procesos[contador_for+1][2]
	procesos[contador_for+1][2] -= procesos[contador_for+1][2]
	if(procesos[contador_for+1][2] == 0):
		tiempo_Final.append([procesos[contador_for+1][0],contador])

	tiempo_Final.sort()	

	for i in range(len(procesos)):
		T.append(tiempo_Final[i][1]-lista[i][1])
		E.append(T[i] - tiempo_requerido[i])
		P.append(T[i]/tiempo_requerido[i])

	TT = sum(T)/len(procesos)
	TE = sum(E)/len(procesos)
	TP = sum(P)/len(procesos)

	print("SPN: T=%.2f, E=%.2f, P=%.2f"%(TT,TE,TP))
	print(orden_ejecucion)
	print(len(orden_ejecucion))


#Forma de elegir para el caso de ejemplo
print("1:Ocupar la lista del ejemplo de clase Selecciona \n2:Generar cargas aleatorias")
entrada = int(input())

#Se ejecuta el caso de ejemplo
if(entrada == 1):
	procesos = [['A', 0, 3], ['B', 1, 5], ['C', 3, 2], ['D', 9, 5], ['E', 12, 5]] 
	print(procesos)
	FCFS(procesos)
	procesosNew = RR(procesos) #Regresa la lista sin modificaciones, para que el siguiente algoritmo la pueda utilizar.
	procesosNew = RR4(procesosNew)
	SPN(procesosNew)

#Se crean procesos de forma aleatoria
if(entrada == 2):
	for i in range(random.randint(1,9)):
		print("==========Número de carga:%d=========="%(i+1))
		listaProcesos = CrearProcesosBase()
		print(listaProcesos)
		FCFS(listaProcesos)
		procesosNew = RR(listaProcesos)
		procesosNew = RR4(procesosNew)
		SPN(procesosNew)


