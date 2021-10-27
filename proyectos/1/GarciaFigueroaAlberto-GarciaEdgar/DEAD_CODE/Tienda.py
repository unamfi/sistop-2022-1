import threading
import sys
import time
import random
from CODE.Cliente import Cliente
from CODE.Empleado import Empleado
from CODE.Proveedor import Proveedor
class Tienda(object):
    
    #Declaramos los productos que se venden en la tienda
    productos = {1:["disfraz de Dracula","Disfraz de zombie","disfraz de hombre lobo","disfraz de momia"], 2:["chocolate","caramelo","milkyway","pikafresas"]}
    contadorPersonas=0
    def __init__(self,nombre,aforo):
        global entradaTorniquete
        entradaTorniquete = threading.Semaphore(1)
        self.nombre = nombre
        self.aforo = aforo
        self.estante=100
        self.estanteMutex=threading.Semaphore(1)
        self.cajaMutex=threading.Semaphore(1)      


    #Dejamos pasar al cliente en cola
    def pass_client(self, cliente):
        global entradaTorniquete
        if Tienda.contadorPersonas<self.aforo:
            entradaTorniquete.acquire()
            Tienda.contadorPersonas+=1
            entradaTorniquete.release()
            print("El cliente "+str(cliente.numero)+" ha entrado a la tienda")
            cliente.agarra()
        else:    
            print("Por restricciones sanitarias el cliente "+str(cliente.numero)+"deberá esperar a que salga un cliente")
    
    def generarCompra(self,cliente):
        
    
    def leave_client(self, cliente):
        global entradaTorniquete
        entradaTorniquete.acquire()
        Tienda.contadorPersonas-=1
        entradaTorniquete.release()
        print("El cliente "+str(cliente.numero)+" ha abandonado la tienda")
    
    def abrir(self):
        listaClientes=[]
        listaEmpleados=[]
        listaProveedores=[]
        print("La tienda ha abierto")
        visitas= random.randint(1,2)
        empleados= random.randint(3,6)
        for k in range (2):
            listaProveedores.append(Proveedor(k,self))
            time.sleep(1)
            threading.Thread(target=listaProveedores[k].run).start()
        for j in range (empleados):
            listaEmpleados.append(Empleado(j,self))
            time.sleep(2)
            threading.Thread(target=listaEmpleados[j].run).start()
        for i in range(visitas):
            listaClientes.append(Cliente(i,self))
            threading.Thread(target=listaClientes[i].entrar).start()