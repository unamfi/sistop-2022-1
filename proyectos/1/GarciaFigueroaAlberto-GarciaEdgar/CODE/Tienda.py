import threading
import sys
import time
import random
from CODE.Cliente import Cliente
from CODE.Empleado import Empleado
class Tienda(object):
    #Declaramos los productos que se venden en la tienda
    productos = {1:["disfraz de Dracula","Disfraz de zombie","disfraz de hombre lobo","disfraz de momia"], 2:["chocolate","caramelo","milkyway","pikafresas"]}
    
    def __init__(self,nombre,aforo):
        global estante
        self.nombre = nombre
        self.aforo = aforo
        self.estante=100
        self.estanteMutex=threading.Semaphore(1)
        self.cajaMutex=threading.Semaphore(1) 
        self.entradaTorniquete= threading.Semaphore(0)
        

    #Dejamos pasar al cliente en cola
    def pass_client(self, cliente):
        if self.aforo<11:
            print("Bienvenido a la tienda cliente numero"+self.visita+" a la tienda")
            aforo =  self.aforo + 1
        else:
            print("Por restricciones sanitarias, deberá esperar a que salga un cliente")
    
    
    def abrir(self):
        listaClientes=[]
        listaEmpleados=[]
        print("La tienda ha abierto")
        visitas= random.randint(4,20)
        empleados= random.randint(3,20)
        for j in range (empleados):
            listaEmpleados.append(Empleado(j,self))
            threading.Thread(target=listaEmpleados[j].run).start()
        for i in range(visitas):
            listaClientes.append(Cliente(i,self))
            threading.Thread(target=listaClientes[i].entrar).start()
            print("Ingresa cliente"+str(i))