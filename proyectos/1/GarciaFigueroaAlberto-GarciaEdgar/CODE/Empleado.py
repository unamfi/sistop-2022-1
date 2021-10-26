import sys
import time
import random
from CODE.Cliente import Cliente
from CODE.Tienda import Tienda
from CODE.Proveedor import Proveedor

class Empleado(object):
    def __init__(self,id):
        self.id = id
    def vender(self, cliente):
        print("Empleado "+self.id+" entrega ticket y producto a "+cliente.numero)
    
    def checarEstante(self):
        if Tienda.estante<15:
            self.llamarProveedor()
    
    def llamarProveedor(self):
        print("Empleado "+self.id+" solicita a un proovedor")
        Proveedor.suministrar()
        print()
    