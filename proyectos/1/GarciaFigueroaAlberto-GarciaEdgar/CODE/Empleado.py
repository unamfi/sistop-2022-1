import sys
import time
import random
#from CODE.Tienda import Tienda
#from CODE.Proveedor import Proveedor

class Empleado(object):
    def __init__(self,id,tienda):
        self.id = id
        self.tienda=tienda
    
    def run(self):
        self.asignarTarea()
    
    def asignarTarea(self):
        print("Empleado "+str(self.id)+" se prepara para trabajar")
        
    def vender(self, cliente):        
        self.tienda.CajaRelease.acquire()
        self.tienda.CajaEmpleado.release()
        print("Empleado "+str(self.id)+" entrega ticket y producto a ")
    def checarEstante(self):
        if self.tienda.estante<15:
            self.llamarProveedor()
    
    def llamarProveedor(self):
        print("Empleado "+str(self.id)+" solicita a un proovedor")
        print()
   
    