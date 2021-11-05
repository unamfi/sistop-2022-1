# Tarea 3 Comparacion de planificadores
# Implementar FCFS,RR y SPN

import random
import copy

PROCESOS = ["A","B","C","D","E"]
NUM_CARGAS = 5
NUM_PROCESOS = 5

def definir_proceso(proceso):
	inicio = random.randint(0,5)
	duracion = random.randint(2,6)
	return[inicio,duracion,proceso]

#FCFS (FIRST COME, FIRST SERVE)

def fcfs(lista):
	fcfs_lista = copy.deepcopy(lista)
	T = 0.0
	E = 0.0
	P = 1

	fcfs_lista[0].append(fcfs_lista[0][0])
	T = fcfs_lista[0][1]

	for i in range(1,NUM_CARGAS):
		tex = (fcfs_lista[i-1][3] + fcfs_lista[i-1][1] - fcfs_lista[i][0])
		fcfs_lista[i].append(tex + fcfs_lista[i][0])
		E = tex + E
		T = T + tex + fcfs_lista[i][1]
		P = P + (tex + fcfs_lista[i][1]) / fcfs_lista[i][1]
	
	E = E / NUM_CARGAS
	T = T / NUM_CARGAS
	P = P / NUM_CARGAS
	print("FCFS:T = %f E = %f P = %f" % (T,E,P))

	for i in range(0,NUM_CARGAS):
		for g in range(0,fcfs_lista[i][1]):
			print(fcfs_lista[i][2],end=' ')
	
	print()
	print()
	
#RR (ROUND ROBIN)
def rr(lista,q):
	rr_lista = []
	rr_lista = copy.deepcopy(lista)
	orden = []
	queue = []
	t = rr_lista[0][0]
	n = 0
	for i in rr_lista:
		if i[0] == t:
			rr_lista[n].append(0)
			queue.append(i)
		n = n + 1
	r = []
	numero = len(queue)
	started = False
	while True:
		for i in range(0,NUM_CARGAS):
			if started == True:
				break
			if(rr_lista[i][0] <= t + q and rr_lista[i].__len__() < 4):
				rr_lista[i].append(0)
				queue.append(rr_lista[i])

				if(i == NUM_CARGAS - 1):
					started = True
		interr_exe = 0
		n = 0
		for i in queue:
			if n == 0:
				i[1] = i[1] - q
				if i[1] > 0:
					for j in range(0,q):
						a = str(i[2])
						orden.append(a)#print(i[2],end='|')
						interr_exe = interr_exe + 1
				elif i[1] <= 0:
					for j in range(0,q + i[1]):
						a = i[2]
						orden.append(a)#print(i[2],end='|')
						interr_exe = interr_exe + 1
					i[1] = 0
					r.append(i)
				n = 1
			else:
				queue.remove(i)
				i[3] = i[3] + t + interr_exe - i[0]
				i[0] = i[0] + t + interr_exe - i[0]
				queue.insert(n,i)
				n = n + 1
		aux = queue[0]
		queue.remove(aux)
		aux[0] = aux[0] + interr_exe
		queue.append(aux)
		for i in queue:
			if i[1] == 0:
				queue.remove(i)
		if started == True and queue.__len__() == 0:
			print()
			break
		t = t + interr_exe
	P = 0.0
	E = 0.0
	T = 0.0
	for i in range(0,NUM_CARGAS-1):
		for g in range(0,NUM_CARGAS-1):
			if rr_lista[i][2] == r[g][2]:
				T = T + lista[i][1] + r[g][3]
				E = E + r[g][3]
				P = P + (lista[i][1] + r[g][3]) / lista[i][1]
	E = E / NUM_CARGAS
	T = T / NUM_CARGAS
	P = P / NUM_CARGAS
	print("RR"+str(q)+": ", end=' ')
	print("T = %f E = %f P = %f" % (T,E,P))
	for i in range(0,len(orden)):
		print(orden[i], end = ' ')
	print()
	print()

#SPN (SHORTEST PROCESS NEXT)

def spn(lista):
	spn_lista = copy.deepcopy(lista)
	orden = []
	for h in spn_lista:
		h.append(0)
		h.append(False)
	queue = []
	t = spn_lista[0][0]
	started = False
	while True:
		for i in range(0,NUM_CARGAS):
			if spn_lista[i][0] <= t and spn_lista[i][4] == False:
				spn_lista[i][4] = True
				spn_lista[i][3] = t - spn_lista[i][0]
				queue.append(spn_lista[i])
				if i == NUM_CARGAS - 1:
					started = True
		if queue.__len__() == 0:
			continue
		else:
			punta = queue[0]
		for i in range(0, queue.__len__()):
			if queue[i][1] < punta[1]:
				punta = queue[i]
		for i in range(0, punta[1]):
			a = punta[2]
			orden.append(a)
		queue.remove(punta)
		t = t + punta[1]
		for i in range(0, len(queue)):
			queue[i][3] = queue[i][3] + punta[1]
		if started == True and len(queue) == 0:
			print()
			break
	P = 0.0
	E = 0.0
	T = 0.0

	for g in spn_lista:
		T = T + g[1] + g[3]
		E = E + g[3]
		P = P + (g[1] + g[3]) / g[1]

	E = E / NUM_CARGAS
	T = T / NUM_CARGAS
	P = P / NUM_CARGAS

	print("SPN: T = %f E = %f P = %f" % (T,E,P))
	for i in range(0,len(orden)):
		print(orden[i], end = ' ')
	print()
	print()


def crearCargas():
	
	for i in range (0,NUM_CARGAS-1):
		cargas = []
		print("╔═════════════════════ RONDA "+ str(i+1) +" ═════════════════════╗")
		print()
		for j in range(0,NUM_PROCESOS):
			cargas.append(definir_proceso(PROCESOS[j]))
			print(cargas[j][2]+": " + str(cargas[j][0]) + " t = " + str(cargas[j][1]) + " ; ", end=" ")
			
		print()
		print()
		cargas.sort()
		fcfs(cargas)
		rr(cargas,1)
		rr(cargas,4)
		spn(cargas)
		cargas.clear()


crearCargas()