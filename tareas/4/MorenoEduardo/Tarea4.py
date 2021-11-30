# Tarea 4 Semantica de archivos
# Implementar un sistema interactivo con la interfaz logica de manipulacion
# de un directorio y los archivos que contiene

import sys

global ident_contador


def instrucciones():
	print("Para el manejo de este gestor de archivos se utilizan los siguientes comandos")
	print("- dir → Muestra el directorio")
	print("- open <arch> <modo> → Especifica que operaremos con el archivo de nombre ""arch"", empleando el modo especificado. Entrega un descriptor de archivo numérico.")
	print("- close <descr> → Termina una sesión de trabajo con el archivo referido por el descriptor indicado. Después de un close, cualquier intento por usar ese archivo entregará error.")
	print("- read <descr> <longitud> → Lee la cantidad de bytes especificada")
	print("- write <descr> <longitud> <datos» → Escribe la cantidad de bytes especificada, guardando los datos indicados como parámetro.")
	print("- seek <descr> <ubicacion> → Salta a la ubicación especificada del archivo.")
	print("- quit → Detiene la ejecucin de la simulación")
	print("Modos disponibles para abrir:")
	print("Read → R ")
	print("Write → W ")
	print("Seek → A ")
	print("")

class archivo:
	def __init__(self,nombre,contenido):
		self.nombre = nombre + ".txt"
		self.contenido = contenido
		self.tamanio = sys.getsizeof(contenido)
		self.modo = "S"
		self.identificador = -1
		self.cursor = 0
	def declarar_modo(self,modo):
		global ident_contador
		ident_contador+= 1
		self.modo = modo
		self.identificador = ident_contador
	def eliminar_modo(self):
		self.modo = "S"
		self.identificador = -1



class directorio:
	def __init__(self):
		archivos_lista = []
		nombres = ["time","light","nature","body","darkness","pain","spores","castle"]
		f = open ('texto.txt','r')
		mensaje = f.read()
		mensajes = mensaje.split("\n")
		for i in range(0,len(nombres)):
			arc = archivo(nombres[i],mensajes[i])
			archivos_lista.append(arc)
		f.close()
		self.contenido_directorio = archivos_lista

	def dir_accion(self):
		for i in range(0,len(self.contenido_directorio)):
			print(self.contenido_directorio[i].nombre+" \t  ["+str(self.contenido_directorio[i].tamanio)+"bytes]")
		print()

	def open_accion(self,archivo,modo):
		actual = -1
		for i in range(0,len(self.contenido_directorio)):
			if archivo == self.contenido_directorio[i].nombre:
				actual = i
		if actual != -1:
			aux_modo = self.contenido_directorio[actual].modo
			if (aux_modo == "S") and (str(modo) != "S"):
				if (modo == "R") or (modo == "W") or (modo == "A"):
					self.contenido_directorio[actual].declarar_modo(modo)
					print("Archivo abierto "+self.contenido_directorio[actual].modo+" → "+ str(self.contenido_directorio[actual].identificador))
				else:
					print("Modo Invalido")
			else:
				print("El archivo ya esta abierto en modo: " + self.contenido_directorio[actual].modo)
		else:
			print("Identificador no encontrado")
	def read_opcion(self,descriptor,longitud):
		actual = -1
		for i in range(0,len(self.contenido_directorio)):
			if str(descriptor) == str(self.contenido_directorio[i].identificador):
				if str(self.contenido_directorio[i].modo) == "R":
					actual = i
				else:
					print("No esta en modo de Lectura")
		if actual == -1:
			print("Identificador no encontrado")
		else:
			print(self.contenido_directorio[actual].contenido[0:longitud])

	def write_opcion(self,descriptor,longitud,datos):
		actual = -1
		for i in range(0,len(self.contenido_directorio)):
			if str(descriptor) == str(self.contenido_directorio[i].identificador):
				actual = i
		if actual != -1:
			if str(longitud) == str(len(datos)):
				if self.contenido_directorio[actual].modo == "W":
					lugar = int(self.contenido_directorio[actual].cursor)
					self.contenido_directorio[actual].contenido = str(self.contenido_directorio[actual].contenido[:lugar]) + str(datos) + str(self.contenido_directorio[actual].contenido[lugar:])
					print("Llevado a cabo correctamente")
				else:
					print("El archivo no esta abierto en modo de Escritura")
			else:
				print("Texto ingresado no cumple con la longitud")
		else:
			print("Identificador no encontrado")

	def seek_opcion(self,descriptor,ubicacion):
		actual = -1
		for i in range(0,len(self.contenido_directorio)):
			if str(descriptor) == str(self.contenido_directorio[i].identificador):
				actual = i
		if actual != -1:
			if str.isdigit(ubicacion) == True:
				if self.contenido_directorio[actual].modo == "A":
					if int(ubicacion) > int(self.contenido_directorio[actual].cursor):
						self.contenido_directorio[actual].cursor = ubicacion
						print("Llevado a cabo correctamente")
					else:
						print("Ubicacion fuera de rango")
				else:
					print("El archivo no esta abierto en modo Busqueda")
			else:
				print("Ubicacion imposible")
		else:
			print("Identificador no encontrado")

	def close_accion(self,descriptor):
		actual = -1
		for i in range(0,len(self.contenido_directorio)):
			if str(descriptor) == str(self.contenido_directorio[i].identificador):
				actual = i
		if self.contenido_directorio[actual].modo != "S":
			self.contenido_directorio[actual].eliminar_modo()
			print("Archivo Cerrado")
		else:
			if actual == -1:
				print("Identificador no encontrado")
			else:
				print("El archivo esta cerrado")
		
			

	def quit_accion(self):
		exit()

def lectura(instruccion,personal_directory,salida):
	desglose = instruccion.split(" ",4)
	if desglose[0] == "open":
		personal_directory.open_accion(desglose[1],desglose[2])
	elif desglose[0] == "close":
		personal_directory.close_accion(desglose[1])
	elif desglose[0] == "read":
		personal_directory.read_opcion(desglose[1],int(desglose[2]))
	elif desglose[0] == "write":
		personal_directory.write_opcion(desglose[1],desglose[2],desglose[3])
	elif desglose[0] == "seek":
		personal_directory.seek_opcion(desglose[1],desglose[2])
	elif desglose[0] == "quit":
		personal_directory.quit_accion()
	elif desglose[0] == "dir":
		personal_directory.dir_accion()
	else:
		print("Comando Invalido")
		
def gestor():
	global ident_contador
	salida = True
	archivos_directorio = []
	ident_contador = 0
	instrucciones()
	personal_directory = directorio()
	while salida:
		comand = input("→ ")
		lectura(comand,personal_directory,salida)
		
gestor()
